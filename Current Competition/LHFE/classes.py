import os
from typing import Optional, List
from constants import CURRENT_DIR, QUALITY


class Target:
    def __init__(self, full_path: str):
        self.full_path = full_path
        self.file_name = os.path.basename(full_path)
        self.root_path = os.path.join(os.path.split(full_path)[0], os.path.split(full_path)[1])
        self.extension = self.file_name.split('.')[-1]
        self.quality = QUALITY.UNDEFINED

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

    def not_empty(self) -> bool:
        return len(self._stack) > 0

    def get_all(self) -> List[object]:
        return self._stack

    def _key(self, obj):
        return obj


class TargetStack(Stack):
    def push(self, target: Target, force=False) -> bool:
        return super(TargetStack, self).push(target, force)

    def pop(self) -> Optional[Target]:
        return super(TargetStack, self).pop()

    def _key(self, target: Target):
        return target.full_path


class Recipe:
    def __init__(self, name):
        self.name = name

    def run(self, book_name, target: Target, output):
        raise NotImplemented


class RecipeBook:
    def __init__(self, name, known_extensions, recipes: List[Recipe]):
        self.name = name
        self.known_extensions = known_extensions
        self.recipes = recipes

    def run_all(self, target: Target, output):
        for recipe in self.recipes:
            recipe.run(self.name, target, output)

    def _is_relevant(self, file_ext):
        return file_ext in self.known_extensions
