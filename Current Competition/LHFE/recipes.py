import subprocess
import os
import shutil
import config
import utils
from typing import List
from constants import GEN_PREFIX, QUALITY
from classes import Target, Recipe, RecipeOutput

_ALL_EXTENSION = '%ALL%'
_IMG_EXTENSIONS = ['gif', 'png', 'jpg', 'jpeg', 'png', 'bmp']


def run_all_for_target(target: Target, output_list: List[RecipeOutput]) -> None:
    for recipe in _recipe_book:
        if _ALL_EXTENSION in recipe.applicable_extensions or target.extension in recipe.applicable_extensions:
            output = recipe.run(target)  # type: RecipeOutput
            output_list.append(output)


def format_command_output(recipe_name: str, target: Target, recipe_output: RecipeOutput, check_for_flag: bool,
                          command: str, limit_lines: int = None) -> None:
    utils.debug(f'Running command {command} for recipe {recipe_name}')
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = process.communicate()[0].decode('utf-8')
    output = f'{recipe_name}:  ({target.full_path})\n\n'
    if check_for_flag:
        possible_flags = utils.check_for_flag(result)
        for possible_flag in possible_flags:
            recipe_output.quality = QUALITY.HIGH
            flag_str = f'Found possible flag ({possible_flag[0]})\n' \
                       f'{possible_flag[1]}\n'
            output += f'{flag_str}\n'
            config.flag_stack.push(flag_str, True)

    lines = result.split('\n')
    if limit_lines is not None and len(lines) > limit_lines * 2:
        output += '\n'.join(lines[:limit_lines+1]) + '\n[output truncated]\n' + '\n'.join(lines[-limit_lines:])
    else:
        output += result
    recipe_output.add_output(output)


class BinwalkRecipe(Recipe):
    def __init__(self):
        super(BinwalkRecipe, self).__init__('Binwalk recipe', _IMG_EXTENSIONS)

    def run(self, target: Target) -> RecipeOutput:
        recipe_output = RecipeOutput(self)
        out_path = os.path.join(os.path.dirname(target.full_path), f'{GEN_PREFIX}binwalk_{target.file_name}')
        format_command_output(self.name, target, recipe_output, False, f'binwalk -e {target.full_path} --directory "{out_path}"')
        if len(os.listdir(out_path)) > 0:
            recipe_output.quality = QUALITY.MEDIUM
            nested_out_path = os.path.join(out_path, os.listdir(out_path)[0])
            files_to_move = os.listdir(nested_out_path)
            for file_to_move in files_to_move:
                shutil.move(os.path.join(nested_out_path, file_to_move), os.path.join(out_path, file_to_move))
            os.rmdir(nested_out_path)
            utils.enum_and_add_targets(out_path)
        else:
            recipe_output.quality = QUALITY.LOW
            os.rmdir(out_path)
        return recipe_output


class StringsRecipe(Recipe):
    def __init__(self):
        super(StringsRecipe, self).__init__('Strings recipe', [_ALL_EXTENSION])

    def run(self, target: Target) -> RecipeOutput:
        recipe_output = RecipeOutput(self)
        format_command_output(self.name, target, recipe_output, True, f'strings {target.full_path}', 5)
        return recipe_output


_recipe_book = [
    BinwalkRecipe(),
    StringsRecipe()
]
