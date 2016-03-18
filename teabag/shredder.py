import os
import subprocess

import settings


def remove_file(file_path):
    command = ['shred', '-u', '-z', '-n',
               str(settings.file_shred_times), file_path]
    _execute(command)
    if os.path.isfile(file_path):
        raise RuntimeError('File {} has not been removed!'.format(file_path))


def _execute(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    code = process.wait()
    if code != 0:
        raise RuntimeError('Command failed')
    output = [line.decode() for line in process.stdout]
    return ''.join(output)
