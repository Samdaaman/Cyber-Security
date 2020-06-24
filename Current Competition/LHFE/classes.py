import os
from typing import Optional, List
from constants import CURRENT_DIR, QUALITY


class Target:
    def __init__(self, full_path: str):
        self.full_path = full_path
        self.file_name = os.path.basename(full_path)
        self.root_path = os.path.join(os.path.split(full_path)[0], os.path.split(full_path)[1])
        self.extension = self.file_name.split('.')[-1]

    def __str__(self):
        return self.full_path.replace(CURRENT_DIR, '')


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

    def pop_all_copy(self) -> list:
        copy_of_stack = self._stack.copy()
        self._stack.clear()
        return copy_of_stack

    def not_empty(self) -> bool:
        return len(self._stack) > 0

    # def get_all(self) -> List[object]:
    #    return self._stack

    def _key(self, obj):
        return obj


class TargetStack(Stack):
    def push(self, target: Target, force=False) -> bool:
        return super(TargetStack, self).push(target, force)

    def pop(self) -> Optional[Target]:
        return super(TargetStack, self).pop()

    def _key(self, target: Target):
        return target.full_path


class FlagStack(Stack):
    def push(self, flag: str, force=False) -> bool:
        return super(FlagStack, self).push(flag, force)

    def pop(self) -> Optional[str]:
        return super(FlagStack, self).pop()

    def pop_all_copy(self) -> List[str]:
        return super(FlagStack, self).pop_all_copy()


class RecipeOutput:
    def __init__(self, recipe):
        self.recipe = recipe  # type: Recipe
        self._output = []  # type: List[str]
        self.quality = QUALITY.UNDEFINED  # type: QUALITY

    def add_output(self, output: str):
        self._output.append(output)

    def raw(self):
        return self._output


class Recipe:
    def __init__(self, name: str, applicable_extensions: List[str]):
        self.name = name
        self.applicable_extensions = applicable_extensions

    def run(self, target: Target) -> RecipeOutput:
        raise NotImplemented


