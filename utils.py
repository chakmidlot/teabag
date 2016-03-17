import os

import settings


def check_path():
    """
    create path for messages
    if it is not exist
    """

    path = settings.keys_path
    if not os.path.exists(path):
        os.makedirs(path)

def startup_check():
    check_path()
