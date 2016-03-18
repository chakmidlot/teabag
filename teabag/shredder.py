import os
import subprocess


def remove_file(file_path):
    command = ['shred', '-u', '-z', '-n', '7', file_path]
    _execute(command)
    assert not os.path.isfile(file_path)


def _execute(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    code = process.wait()
    if code != 0:
        raise RuntimeError('Command failed')
    output = [line.decode() for line in process.stdout]
    return ''.join(output)
