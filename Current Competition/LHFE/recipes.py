from typing import List
import subprocess
import utils

_all = '%ALL%'


def format_command_output(book_name, recipe_name, fp, command):
    utils.debug(f'Running command {command} for recipe {recipe_name} of {book_name}')
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = process.communicate()
    return f'{book_name}: {recipe_name}  ({fp})\n' \
           f'{result[0].decode("utf-8")}\n' \
           f'{result[1].decode("utf-8")}\n'


class Recipe:
    def __init__(self, name):
        self.name = name

    def run(self, book_name, fp, output):
        raise NotImplemented


class Recipe_Book:
    def __init__(self, name, known_exts, recipes: List[Recipe]):
        self.name = name
        self.known_exts = known_exts
        self.recipes = recipes

    def run_all(self, fp, output):
        for recipe in self.recipes:
            recipe.run(self.name, fp, output)

    def _is_relevant(self, file_ext):
        return file_ext in self.known_exts


def run_all_recipe_books(file_ext, fp, output):
    for recipe_book in _all_recipe_books:
        if file_ext in recipe_book.known_exts or recipe_book.known_exts[0] == _all:
            recipe_book.run_all(fp, output)


class ImageRecipeBook(Recipe_Book):
    def __init__(self):
        super(ImageRecipeBook, self).__init__('ImageRecipeBook', ["png"], [
            BinwalkRecipe()
        ])


class BinwalkRecipe(Recipe):
    def __init__(self):
        super(BinwalkRecipe, self).__init__('Binwalk recipe')

    def run(self, book_name, fp, output):
        output.append(format_command_output(book_name, self.name, fp, f'binwalk {fp}'))


_all_recipe_books = [
    ImageRecipeBook()
]
