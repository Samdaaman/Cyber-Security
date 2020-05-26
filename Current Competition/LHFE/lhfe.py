import os
import exceptions
from constants import NEW_DIR, CURRENT_DIR, SOLVED_DIR
from typing import Optional
from exceptions import FatalException
import input
import recipes
import lhfe
from stack import Stack


Instance = None  # type: Optional[LHFE]


def process_file(fp):
    print(f'Processing file {fp}')
    path_parts = os.path.split(fp)
    folder_path = path_parts[:-1]
    file_name = path_parts[-1]
    file_ext = file_name.split('.')[-1]
    output = []
    recipes.run_all_recipe_books(file_ext, fp, output)
    for line in output:
        print(line)



def _check():
    paths = [NEW_DIR, CURRENT_DIR, SOLVED_DIR]
    for path in paths:
        if not os.path.isdir(path):
            raise exceptions.PathMissingException(path)


class LHFE:
    def __init__(self, debug):
        global Instance
        self.debug = debug
        _check()
        if Instance is None:
            lhfe.Instance = self
            Instance = self
        else:
            raise FatalException('Why are you making two instances')

        self.file_paths_to_process = Stack()
        _check()
        input.initial_tick()
        for fp in self.file_paths_to_process.pop_all():
            process_file(fp)

    @classmethod
    def start(cls, debug=True):
        print(f'Initialising (debug={debug})')
        print(f'Using dir "{os.getcwd()}"')
        return cls(debug)
