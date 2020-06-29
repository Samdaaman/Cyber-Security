from typing import List
from .classes import Target
from . import config
from .constants import QUALITY

CONTENTS_PAGE_FILENAME = 'contents.md'


def update():
    previous_targets = config.target_stack.get_all_done()
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
                     f'({previous_target.rel_path}.md)')

    with open(CONTENTS_PAGE_FILENAME, 'w') as fh:
        fh.write('\n  '.join(lines))