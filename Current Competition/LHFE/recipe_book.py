import os
import shutil
from typing import List

from .classes import Recipe, Target, RecipeOutput
from .constants import GEN_PREFIX, QUALITY, ALL_EXTENSION
from .incoming import enum_and_add_targets
from .processing import run_shell_command

_IMG_EXTENSIONS = ['gif', 'png', 'jpg', 'jpeg', 'png', 'bmp']


def run_all_for_target(target: Target) -> List[RecipeOutput]:
    output_list = []
    for recipe in all_recipes:
        if ALL_EXTENSION in recipe.applicable_extensions or target.extension in recipe.applicable_extensions:
            output = recipe.run(target)  # type: RecipeOutput
            output_list.append(output)
    return output_list


class FileRecipe(Recipe):
    def __init__(self):
        super(FileRecipe, self).__init__('File recipe', [ALL_EXTENSION])

    def run(self, target: Target) -> RecipeOutput:
        command = f'file {target.rel_path}'
        recipe_output = RecipeOutput(self, command)
        run_shell_command(self.name, recipe_output, False, command)
        return recipe_output


class HeadRecipe(Recipe):
    def __init__(self):
        super(HeadRecipe, self).__init__('Head recipe', [ALL_EXTENSION])

    def run(self, target: Target) -> RecipeOutput:
        command = f'xxd {target.rel_path} | head -n 40'
        recipe_output = RecipeOutput(self, command)
        run_shell_command(self.name, recipe_output, False, command)
        return recipe_output


class TailRecipe(Recipe):
    def __init__(self):
        super(TailRecipe, self).__init__('Tail recipe', [ALL_EXTENSION])

    def run(self, target: Target) -> RecipeOutput:
        command = f'xxd {target.rel_path} | tail -n 40'
        recipe_output = RecipeOutput(self, command)
        run_shell_command(self.name, recipe_output, False, command)
        return recipe_output


class StringsLongRecipe(Recipe):
    def __init__(self):
        super(StringsLongRecipe, self).__init__('Strings (Long) recipe', [ALL_EXTENSION])

    def run(self, target: Target) -> RecipeOutput:
        command = f'strings {target.rel_path} -n 8'
        recipe_output = RecipeOutput(self, command)
        run_shell_command(self.name, recipe_output, False, command, 50)
        return recipe_output


class StringsAllRecipe(Recipe):
    def __init__(self):
        super(StringsAllRecipe, self).__init__('Strings (All) recipe', [ALL_EXTENSION])

    def run(self, target: Target) -> RecipeOutput:
        command = f'strings {target.rel_path}'
        recipe_output = RecipeOutput(self, command)
        run_shell_command(self.name, recipe_output, True, command, 50)
        return recipe_output


class BinwalkRecipe(Recipe):
    def __init__(self):
        super(BinwalkRecipe, self).__init__('Binwalk recipe', _IMG_EXTENSIONS)

    def run(self, target: Target) -> RecipeOutput:
        out_path = os.path.join(os.path.dirname(target.rel_path), f'{GEN_PREFIX}binwalk_{target.file_name}')
        command = f'binwalk -e {target.rel_path} --directory "{out_path}"'
        recipe_output = RecipeOutput(self, command)
        run_shell_command(self.name, recipe_output, False, command)

        if len(os.listdir(out_path)) > 0:
            recipe_output.quality = QUALITY.MEDIUM
            nested_out_path = os.path.join(out_path, os.listdir(out_path)[0])
            files_to_move = os.listdir(nested_out_path)
            for file_to_move in files_to_move:
                shutil.move(os.path.join(nested_out_path, file_to_move), os.path.join(out_path, file_to_move))
            os.rmdir(nested_out_path)
            enum_and_add_targets(out_path, parent_target=target)
        else:
            recipe_output.quality = QUALITY.LOW
            os.rmdir(out_path)
        return recipe_output


all_recipes = [
    FileRecipe(),
    HeadRecipe(),
    TailRecipe(),
    BinwalkRecipe(),
    StringsLongRecipe(),
    StringsAllRecipe()
]
