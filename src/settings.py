keys_path = '/tmp/teabag'

message_id_size = 8

host = '127.0.0.1:8080/'

remove_function = 'shred'

shred_times = 7


# set your own settings which shouldn't affect the project
# in local_settings.py
try:
    from local_settings import *
except ImportError:
    pass
