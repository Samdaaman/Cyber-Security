import subprocess
import utils
import os
from constants import GEN_PREFIX, QUALITY
from classes import Target, Recipe, RecipeBook

_ALL = '%ALL%'


def format_command_output(book_name, recipe_name, target: Target, command):
    utils.debug(f'Running command {command} for recipe {recipe_name} of {book_name}')
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = process.communicate()
    return f'{book_name}: {recipe_name}  ({target.full_path})\n' \
           f'{result[0].decode("utf-8")}\n' \
           f'{result[1].decode("utf-8")}\n'


def run_all_recipe_books(target: Target, output):
    for recipe_book in _all_recipe_books:
        if target.extension in recipe_book.known_extensions or recipe_book.known_extensions[0] == _ALL:
            recipe_book.run_all(target, output)


class ImageRecipeBook(RecipeBook):
    def __init__(self):
        super(ImageRecipeBook, self).__init__('ImageRecipeBook', ["png", "jpg", "jpeg", "bmp", "gif"], [
            BinwalkRecipe()
        ])


class BinwalkRecipe(Recipe):
    def __init__(self):
        super(BinwalkRecipe, self).__init__('Binwalk recipe')

    def run(self, book_name, target: Target, output):
        temp_output = []
        out_path = os.path.join(os.path.dirname(target.full_path), f'{GEN_PREFIX}binwalk_{target.file_name}')
        temp_output.append(format_command_output(book_name, self.name, target, f'binwalk -e {target.full_path} --directory "{out_path}"'))
        if os.path.isdir(out_path):
            target.quality = QUALITY.MEDIUM
            utils.enum_and_add_targets(out_path)
        output.append(f'Quality is {target.quality}')
        [output.append(line) for line in temp_output]


_all_recipe_books = [
    ImageRecipeBook()
]
