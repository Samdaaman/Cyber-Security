import os
import shutil
from .constants import NEW_DIR, CURRENT_DIR, GEN_PREFIX, GIT_KEEP
from . import utils
from .classes import Target
from . import config


def initial_tick():
    for folder in os.scandir(CURRENT_DIR):
        if folder.name == GIT_KEEP:
            continue
        for file in os.scandir(os.path.join(CURRENT_DIR, folder.name)):
            file_path = os.path.join(CURRENT_DIR, folder.name, file.name)
            if file.name[0:len(GEN_PREFIX)] == GEN_PREFIX:
                shutil.rmtree(file_path)
    utils.enum_and_add_targets(CURRENT_DIR, GEN_PREFIX)
    utils.debug('Completed initial tick')


def tick() -> bool:
    added_at_least_one = False
    utils.debug('tick start')
    for a_file in os.scandir(NEW_DIR):
        if a_file.name == GIT_KEEP:
            continue
        file_path = os.path.join(NEW_DIR, a_file.name)
        if os.path.isfile(file_path):
            file_name_parts = a_file.name.split('_')
            try:
                assert len(file_name_parts) > 1
                assert file_name_parts[0][0] == 'c'
                number = int(file_name_parts[0][1:])
                assert number > 0
                new_file_name = '_'.join(file_name_parts[1:])
                new_root_dir = os.path.join(CURRENT_DIR, f'c{number}')
                if not os.path.isdir(new_root_dir):
                    os.mkdir(new_root_dir)
                new_path = os.path.join(new_root_dir, new_file_name)
                os.rename(file_path, new_path)
                added = config.target_stack.push(Target(new_path))
                added_at_least_one = added_at_least_one or added
            except:
                pass

    # Enumerate current targets
    # added_at_least_one = utils.enum_and_add_targets(CURRENT_DIR, GEN_PREFIX)

    utils.debug('tick end')
    return added_at_least_one


def _move_file(old_fn, new_fn, num):
    old_path = os.path.join(NEW_DIR, old_fn)
    new_dir = os.path.join(CURRENT_DIR, f'c{num}')
    new_path = os.path.join(new_dir, new_fn)
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    os.rename(old_path, new_path)
    return new_path


def _process_file(fn: str):
    if fn[0] == 'c':
        try:
            fn_parts = fn.split('_')
            num_str = fn_parts[0][1:]
            assert len(num_str) > 0
            num = int(num_str)
            return '_'.join(fn_parts[1:]), num
        except:
            pass

    return fn, input(f'Enter challenge number for file={fn}: ')

