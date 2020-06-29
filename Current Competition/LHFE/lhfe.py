import os
from . import singletons, recipe_book
from . import exceptions
from .constants import NEW_DIR, CURRENT_DIR, SOLVED_DIR
from . import incoming
from .classes import Target
from . import outgoing


def enumerate_target(target: Target):
    print(f'Processing target {target}')
    recipe_outputs = recipe_book.run_all_for_target(target)
    outgoing.add_output(target, recipe_outputs)


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

        while singletons.target_stack.not_empty():
            while singletons.target_stack.not_empty():
                next_target = singletons.target_stack.pop()
                enumerate_target(next_target)
            incoming.tick()

    @classmethod
    def start(cls, debug=False):
        print(f'Initialising (debug={debug})')
        singletons.debug = debug
        singletons.dprint(f'Using dir "{os.getcwd()}"')
        return cls()
