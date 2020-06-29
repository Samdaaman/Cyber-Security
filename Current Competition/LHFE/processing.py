import re
import subprocess
from typing import List, Tuple
from . import singletons
from .constants import QUALITY
from .classes import RecipeOutput


def run_shell_command(recipe_name: str, recipe_output: RecipeOutput, check_for_flag: bool, command: str, limit_lines: int = None) -> None:
    singletons.dprint(f'Running command "{command}" for recipe {recipe_name}')
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = process.communicate()[0].decode('utf-8')

    if check_for_flag:
        possible_flags = _check_for_flag(result)
        for possible_flag in possible_flags:
            recipe_output.quality = QUALITY.HIGH
            recipe_output.add_flag(possible_flag)

    lines = result.split('\n')
    if limit_lines is not None and len(lines) > limit_lines * 2:
        lines = lines[:limit_lines+1] + ['[##### output truncated ######]'] + lines[-limit_lines:]
    for line in lines:
        recipe_output.add_output(line)


def _check_for_flag(raw_string: str) -> List[Tuple[str, str]]:
    search_strings = ['flag', 'galf']
    regexes = [(r"[a-zA-Z0-9]{4}:[a-zA-Z0-9]{12}", 0), (r"[a-zA-Z0-9]{12}:[a-zA-Z0-9]{4}", 1)]
    results = []
    for search_str in search_strings:
        if search_str in raw_string:
            index = raw_string.index(search_str)
            around = raw_string[max(0, index - 15): min(len(raw_string), index + 18)]
            results.append((f'Found {search_str} in output', around))

    for regex, key in regexes:
        founds = re.findall(regex, raw_string)
        founds_no_duplicates = []  # type: List[str]
        for found in founds:
            if found not in founds_no_duplicates:
                founds_no_duplicates.append(found)
        for found in founds_no_duplicates:
            results.append((f'Found matching regex: {regex}', found))
            if key == 0:
                _enumerate_common_ciphers(found, results)
            elif key == 1:
                _enumerate_common_ciphers(found[::-1], results)
                results.append(('When reversed we get: ', found[::-1]))
    return results


def _enumerate_common_ciphers(flag_str: str, flag_results: List[Tuple[str, str]]):
    # caesar cipher
    alphabet_caesar = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(1, 25):
        caesar_shifted_flag = ''
        for char in flag_str:
            if char in alphabet_caesar:
                caesar_shifted_flag += alphabet_caesar[(alphabet_caesar.index(char) + i) % len(alphabet_caesar)]
            else:
                caesar_shifted_flag += char
        if 'flag:' in caesar_shifted_flag:
            flag_results.append((f'When Caesar shifted by {i} we got:', caesar_shifted_flag))

    # affine cipher
    alphabet_affine = 'abcdefghijklmnopqrstuvwxyz'
    for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        for b in range(26):
            if a == 1 and b == 0:
                continue
            c = _invmod(a, 26)
            if c == 0:
                print(f'Error: invmod failed for a={a} and b={b}')
                continue

            affine_flag = ''
            for char in flag_str:
                if char in alphabet_affine:
                    affine_flag += alphabet_affine[c * (alphabet_affine.index(char) - b) % 26]
                else:
                    affine_flag += char
            if 'flag:' in affine_flag:
                flag_results.append((f'When Affine decrypted with a={a} and b={b} we got:', affine_flag))


def _invmod(a, b):
    return 0 if a == 0 else 1 if b % a == 0 else b - _invmod(b % a, a) * b // a

