import os
import config
import exceptions
from constants import NEW_DIR, CURRENT_DIR, SOLVED_DIR, QUALITY
import incoming
import recipes
from classes import Target
import utils
import contents_page


def enumerate_target(target: Target):
    print(f'Processing target {target}')
    recipe_outputs = recipes.run_all_for_target(target)

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

    with open(os.path.join(target.folder, f'{target.file_name}.md'), 'w') as fh:
        fh.write('  \n'.join(output_lines))

    contents_page.update()


def _check():
    paths = [NEW_DIR, CURRENT_DIR, SOLVED_DIR]
    for path in paths:
        if not os.path.isdir(path):
            raise exceptions.PathMissingException(path)


class LHFE:
    def __init__(self):
        _check()

        incoming.initial_tick()
        incoming.tick()

        while config.target_stack.not_empty():
            while config.target_stack.not_empty():
                next_target = config.target_stack.pop()
                enumerate_target(next_target)
            incoming.tick()

    @classmethod
    def start(cls, debug=False):
        print(f'Initialising (debug={debug})')
        config.debug = debug
        utils.debug(f'Using dir "{os.getcwd()}"')
        return cls()
