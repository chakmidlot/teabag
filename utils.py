import os

import settings


def startup_check():
    # create path for messages if it is not exist
    path = settings.keys_path
    if not os.path.exists(path):
        os.makedirs(path)
