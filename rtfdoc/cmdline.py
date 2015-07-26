import os
import sys
import fnmatch

from rtfdoc import html
from rtfdoc.config import get_user_config
from rtfdoc.cmark import transform_markdown_into_html

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


def main(argv):
    current_working_dir = os.getcwd()
    config = get_user_config(current_working_dir)

    sources_dir = os.path.abspath(config['root_dir'])
    for root, dirnames, filenames in os.walk(sources_dir):
        for filename in fnmatch.filter(filenames, '*.md'):
            markdown_file_path = os.path.join(root, filename)

            html_block = transform_markdown_into_html(markdown_file_path)

            template_dir = html.get_template_dir(current_working_dir)

            wrapped_html = html.wrap_html_block(html_block)

            html_content = html.render_html(config, template_dir, wrapped_html)

            html_relative_path = html.get_html_relative_path(markdown_file_path, sources_dir)

            html_file_path = os.path.abspath(os.path.join(config['build_dir'], html_relative_path))
            html.write_html_file(html_content, html_file_path)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
