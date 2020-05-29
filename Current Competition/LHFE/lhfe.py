import os
import config
import exceptions
from constants import NEW_DIR, CURRENT_DIR, SOLVED_DIR
import incoming
import recipes
from classes import Target


def enumerate_target(target: Target):
    print(f'Processing target {target}')
    output = []
    recipes.run_all_recipe_books(target, output)
    for line in output:
        print(line)


def _check():
    paths = [NEW_DIR, CURRENT_DIR, SOLVED_DIR]
    for path in paths:
        if not os.path.isdir(path):
            raise exceptions.PathMissingException(path)


class LHFE:
    def __init__(self, debug):
        self.debug = debug
        _check()

        incoming.initial_tick()
        incoming.tick()

        while config.target_stack.not_empty():
            while config.target_stack.not_empty():
                next_target = config.target_stack.pop()
                enumerate_target(next_target)
            incoming.tick()

    @classmethod
    def start(cls, debug=True):
        print(f'Initialising (debug={debug})')
        print(f'Using dir "{os.getcwd()}"')
        return cls(debug)
