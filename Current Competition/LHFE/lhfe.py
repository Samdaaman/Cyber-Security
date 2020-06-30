import os
from . import singletons, recipe_book
from . import exceptions
from .constants import NEW_DIR, CURRENT_DIR
from . import incoming
from .classes import Target
from . import outgoing


def enumerate_target(target: Target):
    print(f'Processing target {target}')
    recipe_outputs = recipe_book.run_all_for_target(target)
    outgoing.add_output(target, recipe_outputs)


def _check():
    paths = [NEW_DIR, CURRENT_DIR]
    for path in paths:
        if not os.path.isdir(path):
            raise exceptions.PathMissingException(path)


def _process_targets():
    while singletons.target_tracker.not_empty():
        while singletons.target_tracker.not_empty():
            next_target = singletons.target_tracker.pop()
            enumerate_target(next_target)


def _process_commands():
    # Blocks and holds for any command that is not refreshing
    while True:
        command = input('\nEnter command (r=refresh, d=delete): ')
        if command == 'r':
            break
        elif command == 'd':
            delete_able_targets = singletons.target_tracker.get_done_root_targets()
            if len(delete_able_targets) > 0:
                for i in range(len(delete_able_targets)):
                    print(f'Target #{str(i).ljust(2)} - {delete_able_targets[i].rel_path}')
                try:
                    number = int(input('Enter target #: '))
                    removed_targets = singletons.target_tracker.remove_done_root_target_and_children(delete_able_targets[number])
                    outgoing.remove_outputs(removed_targets)
                    for removed_target in removed_targets:
                        incoming.delete_target_files(removed_target)
                    print(f'Removed {len(removed_targets)} targets successfully')
                except Exception as ex:
                    print(f'Error {ex.args[0]}')
                    raise ex
            else:
                print('No deletable targets')


def start(debug=False):
    print(f'Initialising (debug={debug})')
    singletons.debug = debug
    singletons.dprint(f'Using dir "{os.getcwd()}"')
    _check()

    incoming.initial_tick()
    incoming.tick()
    _process_targets()

    while True:
        _process_commands()
        try:
            if incoming.tick():
                _process_targets()
        except KeyboardInterrupt:
            print('Keyboard interrupt, going back to console')
