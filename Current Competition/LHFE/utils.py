import config
import os
from typing import List
from classes import Target
from constants import GIT_KEEP


def debug(string: str) -> None:
    if config.debug:
        print(string)


def enum_dir_recursive(directory: str, ignore_prefix: str = None, reverse=True) -> List[str]:
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


def enum_and_add_targets(directory: str, ignore_prefix: str = None) -> bool:
    file_paths = enum_dir_recursive(directory, ignore_prefix)
    added_at_least_one = False
    for file_path in file_paths:
        added = config.target_stack.push(Target(file_path))
        added_at_least_one = added_at_least_one or added
    return added_at_least_one
