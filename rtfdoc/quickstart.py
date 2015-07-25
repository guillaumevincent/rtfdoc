import os
import sys
import configparser

from rtfdoc import __version__
from rtfdoc.constants import config_file_name


class ValidationError(Exception):
    """Raised for validation errors."""


def nonempty(value):
    if not value:
        raise ValidationError("Please enter some value.")
    return value


def empty(value):
    return value


def do_prompt(config, key, text, default=None, validator=nonempty):
    value = ''
    while True:
        if default:
            prompt = '{} [{}]: '.format(text, default)
        else:
            prompt = '{}: '.format(text, default)
        value = input(prompt).strip()
        if default and not value:
            value = default

        try:
            value = validator(value)
        except ValidationError as err:
            print('* ' + str(err))
            continue
        break
    config[key] = value
    print()


def ask_user(config):
    print('# Welcome to the rtfdoc {} quickstart utility.'.format(__version__))
    print('''
Please enter values for the following settings
(just press Enter to accept a default value, if one is given in brackets).''')
    print()
    print('Enter the root directory for documentation.')
    do_prompt(config, 'root_dir', 'Root directory for the documentation', '.')

    if os.path.isfile(os.path.join(config['root_dir'], config_file_name)):
        print()
        print('''Error: an existing rtfdoc.conf has been found in the selected root directory.
rtfdoc-quickstart will not overwrite existing config. Move {} and restart rtfdoc-quickstart.'''.format(
            config_file_name))
        print()
        sys.exit(1)

    if 'build_dir' not in config:
        print('Enter the build directory for rtfdoc output.')
        do_prompt(config, 'build_dir', 'Build directory for the documentation', '_build')

    if 'project_name' not in config:
        print('The project name will occur in several places in the built documentation.')
        do_prompt(config, 'project', 'Project name')

    if 'authors' not in config:
        do_prompt(config, 'authors', 'Author name(s)')

    if 'version' not in config:
        do_prompt(config, 'version', 'Version of your documentation', 'v1.0.0')

    if 'versions' not in config:
        print('''rtfdoc can build different versions of your documentation.
Each version should correspond to a git reference (tag or branch name).
Specify every version with its tag or branch name separated by colon (ex: master,v1.0.0).
Leave empty, if you don't want to build other version''')
        do_prompt(config, 'versions', 'Other versions', '', empty)

    if 'default_language' not in config:
        print('Add the default language of your documentation.')
        do_prompt(config, 'default_language', 'Default language', 'en')

    if 'languages' not in config:
        print('''rtfdoc can build documentation for differents languages.
You just need to specify one or more language separated by colon (ex: fr,it,es).
A language should correspond to a folder in the root directory.''')
        do_prompt(config, 'languages', 'Other languages', '', empty)

    if 'master_document' not in config:
        print('''rtfdoc need a master document.
It corresponds to the root of the hierarchical structure of the documentation. ''')
        do_prompt(config, 'master_document', 'Name of your master document', 'index.md')


def generate(data):
    config = configparser.ConfigParser()
    config['RTFDOC'] = data

    with open(config_file_name, 'w') as configfile:
        config.write(configfile)


def main(argv=sys.argv):
    config = {}
    ask_user(config)
    generate(config)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
