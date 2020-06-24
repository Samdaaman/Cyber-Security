import config
import os
import re
from typing import List, Tuple
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


def check_for_flag(raw_string: str) -> List[Tuple[str, str]]:
    search_strings = ['flag', 'galf']
    regexes = [r"[a-zA-Z0-9]{4}:[a-zA-Z0-9]{8,14}", r"[a-zA-Z0-9]{8,14}:[a-zA-Z0-9]{4}"]
    results = []
    for search_str in search_strings:
        if search_str in raw_string:
            index = raw_string.index(search_str)
            around = raw_string[max(0, index - 16): min(len(raw_string), index + 20)]
            results.append((f'Found {search_str} in output', around))

    for regex in regexes:
        for found in re.compile(regex).findall(raw_string):
            results.append((f'Found matching regex:', found))

    return results
