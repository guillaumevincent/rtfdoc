import os

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

from rtfdoc.constants import config_file_name


def get_user_config(config_dir):
    config_file_path = os.path.join(config_dir, config_file_name)
    if not os.path.isfile(config_file_path):
        print('Error: Cannot find config file {} in directory {}'.format(config_file_name, config_dir))
        print('Run rtfdoc-quickstart first.')
        return 1
    config = configparser.ConfigParser()
    config.read(config_file_path)
    return dict(config.items('RTFDOC'))
