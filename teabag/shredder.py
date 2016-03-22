import os

import settings
import utils


def _shred_remove_file(file_path):
    shred_times = str(settings.shred_times)
    command = ['shred', '-u', '-z', '-n', shred_times, file_path]
    utils.shell_execute(command)


def _os_remove_file(file_path):
    os.remove(file_path)


def remove_file(file_path):
    """
    main remove function
    """

    remove_func = REMOVE_FUNCS.get(settings.remove_function, _os_remove_file)
    remove_func(file_path)
    if os.path.isfile(file_path):
        raise RuntimeError('File {} has not been removed!'.format(file_path))


REMOVE_FUNCS = {
    'shred': _shred_remove_file,
    'os': _os_remove_file
}
