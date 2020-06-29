import subprocess
import os
import shutil
from . import config
from . import utils
from typing import List
from .constants import GEN_PREFIX, QUALITY
from .classes import Target, Recipe, RecipeOutput

_ALL_EXTENSION = '%ALL%'
_IMG_EXTENSIONS = ['gif', 'png', 'jpg', 'jpeg', 'png', 'bmp']


def run_all_for_target(target: Target) -> List[RecipeOutput]:
    output_list = []
    for recipe in _recipe_book:
        if _ALL_EXTENSION in recipe.applicable_extensions or target.extension in recipe.applicable_extensions:
            output = recipe.run(target)  # type: RecipeOutput
            output_list.append(output)
    return output_list


def format_command_output(recipe_name: str, recipe_output: RecipeOutput, check_for_flag: bool, command: str, limit_lines: int = None) -> None:
    utils.debug(f'Running command {command} for recipe {recipe_name}')
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = process.communicate()[0].decode('utf-8')

    if check_for_flag:
        possible_flags = utils.check_for_flag(result)
        for possible_flag in possible_flags:
            recipe_output.quality = QUALITY.HIGH
            recipe_output.add_flag(possible_flag)

    lines = result.split('\n')
    if limit_lines is not None and len(lines) > limit_lines * 2:
        lines = lines[:limit_lines+1] + ['[##### output truncated ######]'] + lines[-limit_lines:]
    for line in lines:
        recipe_output.add_output(line)


class BinwalkRecipe(Recipe):
    def __init__(self):
        super(BinwalkRecipe, self).__init__('Binwalk recipe', _IMG_EXTENSIONS)

    def run(self, target: Target) -> RecipeOutput:
        out_path = os.path.join(os.path.dirname(target.rel_path), f'{GEN_PREFIX}binwalk_{target.file_name}')
        command = f'binwalk -e {target.rel_path} --directory "{out_path}"'
        recipe_output = RecipeOutput(self, command)
        format_command_output(self.name, recipe_output, False, command)

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
        command = f'strings {target.rel_path}'
        recipe_output = RecipeOutput(self, command)
        format_command_output(self.name, recipe_output, True, command, 50)
        return recipe_output


_recipe_book = [
    BinwalkRecipe(),
    StringsRecipe()
]
