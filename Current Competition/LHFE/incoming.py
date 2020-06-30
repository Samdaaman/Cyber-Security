import os
import shutil
from typing import List
from . import singletons
from .constants import NEW_DIR, CURRENT_DIR, GEN_PREFIX, GIT_KEEP
from .classes import Target


def initial_tick():
    for folder in os.scandir(CURRENT_DIR):  # type: os.DirEntry
        if folder.name[0:len(GEN_PREFIX)] == GEN_PREFIX:
            shutil.rmtree(folder.path)

    enum_and_add_targets(CURRENT_DIR, GEN_PREFIX)
    singletons.dprint('Completed initial tick')


def tick() -> bool:
    added_at_least_one = False
    singletons.dprint('tick start')
    files = [file for file in os.scandir(NEW_DIR)]  # type: List[os.DirEntry]
    files.sort(key=os.path.getctime)
    for file in files:
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
    if os.path.isfile(target.rel_path):
        os.unlink(target.rel_path)

    if target.folder != CURRENT_DIR and os.path.isdir(target.folder) and len([file for file in os.scandir(target.folder)]) == 0:
        os.rmdir(target.folder)

    new_path = os.path.join(NEW_DIR, target.file_name)
    if os.path.isfile(new_path):
        os.unlink(new_path)


def enum_and_add_targets(directory: str, ignore_prefix: str = None, parent_target: Target = None) -> bool:
    file_paths = _enum_dir_recursive(directory, ignore_prefix)
    added_at_least_one = False
    for file_path in file_paths:
        if os.path.split(file_path)[1] == GIT_KEEP:
            continue
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

