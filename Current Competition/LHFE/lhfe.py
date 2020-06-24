import os
import config
import exceptions
from constants import NEW_DIR, CURRENT_DIR, SOLVED_DIR
import incoming
import recipes
from classes import Target
import utils


def enumerate_target(target: Target):
    print(f'Processing target {target}')
    recipe_outputs = []
    recipes.run_all_for_target(target, recipe_outputs)
    for recipe_output in recipe_outputs:
        for line in recipe_output.raw():
            continue
            print(line)

    for flag in config.flag_stack.pop_all_copy():
        print(flag)


def _check():
    paths = [NEW_DIR, CURRENT_DIR, SOLVED_DIR]
    for path in paths:
        if not os.path.isdir(path):
            raise exceptions.PathMissingException(path)


class LHFE:
    def __init__(self):
        _check()

        incoming.initial_tick()
        incoming.tick()

        while config.target_stack.not_empty():
            while config.target_stack.not_empty():
                next_target = config.target_stack.pop()
                enumerate_target(next_target)
            incoming.tick()

    @classmethod
    def start(cls, debug=False):
        print(f'Initialising (debug={debug})')
        config.debug = debug
        utils.debug(f'Using dir "{os.getcwd()}"')
        return cls()
