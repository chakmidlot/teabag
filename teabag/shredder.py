import os

import settings
import utils


def shred_remove_file(file_path):
    command = ['shred', '-u', '-z', '-n', str(settings.shred_times), file_path]
    utils.shell_execute(command)


def os_remove_file(file_path):
    os.remove(file_path)


def remove_file(file_path):
    remove_func = REMOVE_FUNCS.get(settings.remove_function, os_remove_file)
    remove_func(file_path)
    if os.path.isfile(file_path):
        raise RuntimeError('File {} has not been removed!'.format(file_path))


REMOVE_FUNCS = {
    'shred': shred_remove_file,
    'os': os_remove_file
}
