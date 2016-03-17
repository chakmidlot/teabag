import os

import settings


def check_path():
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

    check_path()
