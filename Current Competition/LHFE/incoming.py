import os
import shutil
from typing import List
from . import singletons
from .constants import NEW_DIR, CURRENT_DIR, GEN_PREFIX, GIT_KEEP
from .classes import Target


def initial_tick():
    for folder in os.scandir(CURRENT_DIR):
        if folder.name == GIT_KEEP:
            continue
        for file in os.scandir(os.path.join(CURRENT_DIR, folder.name)):
            file_path = os.path.join(CURRENT_DIR, folder.name, file.name)
            if file.name[0:len(GEN_PREFIX)] == GEN_PREFIX:
                shutil.rmtree(file_path)
    enum_and_add_targets(CURRENT_DIR, GEN_PREFIX)
    singletons.dprint('Completed initial tick')


def tick() -> bool:
    added_at_least_one = False
    singletons.dprint('tick start')
    for file in os.scandir(NEW_DIR):
        if file.name == GIT_KEEP:
            continue
        new_file_path = os.path.join(NEW_DIR, file.name)
        current_file_path = os.path.join(CURRENT_DIR, file.name)
        if os.path.isfile(new_file_path) and not os.path.isfile(current_file_path):
            shutil.copyfile(new_file_path, current_file_path)
            added = singletons.target_tracker.push(Target(current_file_path))
            added_at_least_one = added_at_least_one or added
            print(f'Adding {current_file_path} to target stack')
    singletons.dprint('tick end')
    return added_at_least_one


def delete_target_files(target: Target):
    if target.folder != CURRENT_DIR:
        shutil.rmtree(target.folder)
    else:
        if os.path.isfile(target.rel_path):
            os.unlink(target.rel_path)

    new_path = os.path.join(NEW_DIR, target.file_name)
    if os.path.isfile(new_path):
        os.unlink(new_path)


def enum_and_add_targets(directory: str, ignore_prefix: str = None, parent_target: Target = None) -> bool:
    file_paths = _enum_dir_recursive(directory, ignore_prefix)
    added_at_least_one = False
    for file_path in file_paths:
        target = Target(file_path, parent_target)
        added = singletons.target_tracker.push(target)
        if parent_target is not None and added:
            parent_target.child_targets.append(target)
        added_at_least_one = added_at_least_one or added
    return added_at_least_one


def _enum_dir_recursive(directory: str, ignore_prefix: str = None, reverse=True) -> List[str]:
    file_paths = []
    for root_dir, sub_dirs, file_names in os.walk(directory):
        for file_name in file_names:
            if file_name == GIT_KEEP:
                continue
            ignore = False
            if ignore_prefix is not None:
                for file_path_part in os.path.normpath(os.path.join(root_dir, file_name)).split(os.path.sep):
                    if file_path_part.startswith(ignore_prefix):
                        ignore = True
                        break

            if not ignore:
                file_paths.append(os.path.join(root_dir, file_name))
    if not reverse:
        file_paths.reverse()
    return file_paths


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

