import os
from typing import List

from . import singletons
from .classes import Target, RecipeOutput
from .constants import QUALITY, GEN_PREFIX

CONTENTS_PAGE_FILENAME = 'contents.md'


def get_file_name_for_target(target: Target):
    return f'{os.path.join(os.path.split(target.rel_path)[0], GEN_PREFIX + os.path.split(target.rel_path)[1])}.md'


def remove_outputs(targets: List[Target]):
    for target in targets:
        if os.path.isfile(get_file_name_for_target(target)):
            os.unlink(get_file_name_for_target(target))
    _contents_page_update()


def add_output(target: Target, recipe_outputs: List[RecipeOutput]):
    folders = []
    path = target.folder
    while 1:
        path, folder = os.path.split(path)

        if folder != "":
            folders.append(folder)
        else:
            if path != "":
                folders.append(path)
            break

    for recipe_output in recipe_outputs:
        if target.highest_quality == QUALITY.UNDEFINED:
            target.highest_quality = recipe_output.quality
        elif target.highest_quality == QUALITY.LOW and recipe_output.quality != QUALITY.UNDEFINED:
            target.highest_quality = recipe_output.quality
        elif target.highest_quality == QUALITY.MEDIUM and recipe_output.quality not in [QUALITY.UNDEFINED, QUALITY.LOW]:
            target.highest_quality = recipe_output.quality

    output_lines = [
        f'[Go back to contents]({"../" * len(folders)}contents.md)',
        f'# Target: {target.file_name}  -  Quality: {target.highest_quality}',
        f'## Path: {target.rel_path}',
        f'---',
        f'## Possible flags:',
    ]

    for recipe_output in recipe_outputs:
        for flag in recipe_output.possible_flags:
            output_lines.append(f' - {recipe_output.recipe.name} ({flag[0]}): ``{flag[1]}``')

    output_lines.append('')
    output_lines.append('---')
    output_lines.append('&nbsp;')

    for recipe_output in recipe_outputs:
        output_lines.append(f'### Recipe: {recipe_output.recipe.name} - Quality: {recipe_output.quality}')
        output_lines.append(f'#### {recipe_output.description}')
        output_lines.append(f'```')
        for line in recipe_output.formatted():
            output_lines.append(line)
        output_lines.append(f'```')
        output_lines.append('&nbsp;')
        output_lines.append('')

    with open(get_file_name_for_target(target), 'w') as fh:
        fh.write('  \n'.join(output_lines))

    _contents_page_update()


def _contents_page_update():
    previous_targets = singletons.target_tracker.get_all_done()
    lines = [
        f'# Contents',
        f'',
        f'---',
        f''
    ]

    for previous_target in previous_targets:
        hq = previous_target.highest_quality in [QUALITY.MEDIUM, QUALITY.HIGH]
        lines.append(f' - [{"**" if hq else ""}'
                     f'{previous_target.rel_path}'
                     f'  -  Quality: {previous_target.highest_quality}'
                     f'{"**" if hq else ""}]'
                     f'({get_file_name_for_target(previous_target)})')

    with open(CONTENTS_PAGE_FILENAME, 'w') as fh:
        fh.write('\n  '.join(lines))
