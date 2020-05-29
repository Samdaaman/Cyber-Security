import os
from constants import NEW_DIR, CURRENT_DIR, GEN_PREFIX
import utils
import lhfe


def initial_tick():
    for folder in os.scandir(CURRENT_DIR):
        for file in os.scandir(os.path.join(CURRENT_DIR, folder.name)):
            file_path = os.path.join(CURRENT_DIR, folder.name, file.name)
            if file.name[0:len(GEN_PREFIX)] == GEN_PREFIX:
                os.remove(file_path)
            else:
                lhfe.Instance.file_paths_to_process.push(file_path)
    utils.debug('Completed initial input tick')


def tick():
    utils.debug('tick start')
    file_names = [file.name for file in os.scandir(NEW_DIR)]
    for fn in file_names:
        utils.debug(f'Noticed file {fn}, processing....')
        try:
            new_fn, num = _process_file(fn)
            new_path = _move_file(fn, new_fn, num)
            lhfe.Instance.file_paths_to_process.push(new_path)
        except Exception as e:
            print(f'Error processing file {e}')
    utils.debug('tick end')


def _move_file(old_fn, new_fn, num):
    old_path = os.path.join(NEW_DIR, old_fn)
    new_dir = os.path.join(CURRENT_DIR, f'c{num}')
    new_path = os.path.join(new_dir, new_fn)
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    os.rename(old_path, new_path)
    return new_path


def _process_file(fn: str):
    if fn[0] == 'c':
        try:
            fn_parts = fn.split('_')
            num_str = fn_parts[0][1:]
            assert len(num_str) > 0
            num = int(num_str)
            return '_'.join(fn_parts[1:]), num
        except:
            pass

    return fn, input(f'Enter challenge number for file={fn}: ')

