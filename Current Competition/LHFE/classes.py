import os
from typing import Optional, List, Tuple
from .constants import CURRENT_DIR, QUALITY, ALL_EXTENSION


class Target:
    def __init__(self, rel_path: str):
        self.rel_path = rel_path
        self.file_name = os.path.basename(rel_path)
        self.folder = os.path.split(rel_path)[0]
        self.extension = self.file_name.split('.')[-1]
        self.highest_quality = QUALITY.UNDEFINED

    def __str__(self):
        return self.rel_path.replace(CURRENT_DIR, '')


class Stack:
    def __init__(self):
        self._stack = []
        self._done_keys = []

    def push(self, obj, force=True) -> bool:
        if force or self._key(obj) not in self._done_keys:
            self._stack.append(obj)
            return True

    def pop(self) -> Optional[object]:
        if len(self._stack) > 0:
            top = self._stack[len(self._stack) - 1]
            self._stack.remove(top)
            self._done_keys.append(self._key(top))
            return top

    def pop_all(self) -> list:
        copy_of_stack = self._stack.copy()
        self._stack.clear()
        return copy_of_stack

    def not_empty(self) -> bool:
        return len(self._stack) > 0

    # def get_all(self) -> List[object]:
    #    return self._stack

    def _get_done_keys(self) -> list:
        return self._done_keys.copy()

    def _key(self, obj):
        return obj


class TargetStack(Stack):
    def __init__(self):
        super(TargetStack, self).__init__()
        self._done_targets = []  # type: List[Target]

    def push(self, target: Target, force=False) -> bool:
        return super(TargetStack, self).push(target, force)

    def get_all_done(self) -> List[Target]:
        return self._done_targets.copy()

    def pop(self) -> Optional[Target]:
        target = super(TargetStack, self).pop()
        if target is not None and isinstance(target, Target):
            self._done_targets.append(target)
            return target

    def _key(self, target: Target):
        return target.rel_path


class RecipeOutput:
    def __init__(self, recipe, description: str):
        self.recipe = recipe  # type: Recipe
        self.description = description  # type: str
        self._raw_output = []  # type: List[str]
        self._formatted_output = []  # type: List[str]
        self.quality = QUALITY.UNDEFINED  # type: QUALITY
        self.possible_flags = []  # type: List[Tuple[str, str]]

    def add_flag(self, flag: Tuple[str, str]):
        self._raw_output.append(f'Possible flag: {flag[1]} - {flag[0]}')
        # self._formatted_output.append(f'### Possible flag ({flag[0]})')
        # self._formatted_output.append(flag[1])
        # self._formatted_output.append('')
        self.possible_flags.append(flag)

    def add_output(self, output: str, bold: bool = False):
        bold_char = "**"
        self._raw_output.append(output)
        self._formatted_output.append(f'{bold_char if bold else ""}{output}{bold_char if bold else ""}')

    def raw(self):
        return self._raw_output

    def formatted(self):
        return self._formatted_output


class Recipe:
    def __init__(self, name: str, applicable_extensions: List[str]):
        self.name = name
        self.applicable_extensions = applicable_extensions

    def run(self, target: Target) -> RecipeOutput:
        raise NotImplemented

    def applies_to_extension(self, target_extension: str) -> bool:
        return self.applicable_extensions == ALL_EXTENSION or target_extension in self.applicable_extensions
