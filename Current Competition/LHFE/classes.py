import os
from typing import Optional, List, Tuple
from .constants import CURRENT_DIR, QUALITY, ALL_EXTENSION


class Target:
    def __init__(self, rel_path: str, parent_target=None):
        self.rel_path = rel_path
        self.parent_target = parent_target  # type: Target
        self.file_name = os.path.basename(rel_path)
        self.folder = os.path.split(rel_path)[0]
        self.extension = self.file_name.split('.')[-1]
        self.highest_quality = QUALITY.UNDEFINED
        self.child_targets = []  # type: List[Target]

    def __str__(self):
        return self.rel_path.replace(CURRENT_DIR, '')


class TargetTracker:
    def __init__(self):
        self._current_targets = []  # type: List[Target]
        self._done_targets = []  # type: List[Target]

    def push(self, target: Target, force=False) -> bool:
        if force or target.rel_path not in self._done_paths():
            self._current_targets.append(target)
            return True
        print(self._done_paths())

    def get_all_done(self) -> List[Target]:
        return self._done_targets.copy()

    def pop(self) -> Optional[Target]:
        if self.not_empty():
            target = self._current_targets[0]
            self._current_targets.remove(target)
            self._done_targets.append(target)
            return target

    def not_empty(self) -> bool:
        return len(self._current_targets) > 0

    def _done_paths(self) -> List[str]:
        return [target.rel_path for target in self._done_targets]

    def get_done_root_targets(self) -> List[Target]:
        targets = []
        for target in self._done_targets:
            if target.parent_target is None:
                targets.append(target)
        return targets

    def remove_done_root_target_and_children(self, target: Target) -> List[Target]:
        removed_targets = []  # type: List[Target]
        if target in self._done_targets:
            self._done_targets.remove(target)
            removed_targets.append(target)
            for child_target in target.child_targets:
                if child_target in self._done_targets:
                    self._done_targets.remove(child_target)
                    removed_targets.append(child_target)
                else:
                    print(f'Could not remove target {target} as it is not done yet')
        else:
            print(f'Could not remove target {target} as it is not done yet')
        return removed_targets


class RecipeOutput:
    def __init__(self, recipe, description: str):
        self.recipe = recipe  # type: Recipe
        self.description = description  # type: str
        self._raw_output = []  # type: List[str]
        self._formatted_output = []  # type: List[str]
        self.quality = QUALITY.UNDEFINED  # type: QUALITY
        self.possible_flags = []  # type: List[Tuple[str, str]]
        self.image_paths = []  # type: List[str]

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

    def add_image_path(self, image_path: str):
        self.image_paths.append(image_path)

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
