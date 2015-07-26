import os
import sys

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

from rtfdoc import cmark
from rtfdoc.constants import config_file_name


def main(argv):
    try:
        config_dir = os.getcwd()
        config_file_path = os.path.join(config_dir, config_file_name)
        if not os.path.isfile(config_file_path):
            print('Error: Cannot find config file {} in directory {}'.format(config_file_name, config_dir))
            print('Run rtfdoc-quickstart first.')
            return 1

        config = configparser.ConfigParser()
        config.read(config_file_path)

        sources_dir = os.path.abspath(config['RTFDOC']['root_dir'])
        build_dir = os.path.abspath(config['RTFDOC']['build_dir'])

        cmark.convert_dir_to_html(sources_dir, build_dir)
    except Exception:
        print('Error: something bad happend, can you report a bug ?')
        return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
