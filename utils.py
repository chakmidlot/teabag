import os
import subprocess

import settings


def check_keys_path():
    """
    create path for messages
    if it is not exist
    """

    if not os.path.exists(settings.keys_path):
        os.makedirs(settings.keys_path)


def startup_check():
    """
    actions that we should do on startup
    """

    check_keys_path()


def shell_execute(command):
    """
    executes provided command in system shell
    and returns it's output
    """

    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    code = process.wait()
    if code != 0:
        raise RuntimeError('Command failed')
    output = [line.decode() for line in process.stdout]
    return ''.join(output)
