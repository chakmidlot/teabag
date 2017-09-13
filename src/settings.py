keys_path = '../message_store'

message_id_size = 8

remove_function = 'shred'

shred_times = 7


# set your own settings which shouldn't affect the project
# in local_settings.py
try:
    from local_settings import *
except ImportError:
    pass
