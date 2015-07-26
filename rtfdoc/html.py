import os

from jinja2 import Environment, FileSystemLoader


def wrap_html_block(html_block):
    return '{{% extends "base.html" %}}{{% block content %}}{0}{{% endblock %}}'.format(html_block)


def render_html(config, template_dir, wrapped_html):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.from_string(wrapped_html)
    html = template.render(config)
    return html


def write_html_file(html, html_file_path):
    if not os.path.exists(os.path.dirname(html_file_path)):
        os.makedirs(os.path.dirname(html_file_path))
    with open(html_file_path, 'w') as w:
        w.write(html)


def get_html_relative_path(markdown_file_path, sources_dir):
    markdown_relative_path = os.path.relpath(markdown_file_path, sources_dir)
    return os.path.splitext(markdown_relative_path)[0] + '.html'


def get_template_dir(current_working_dir):
    template_dir = os.path.join(current_working_dir, '_assets', 'templates')
    if not os.path.exists(template_dir):
        template_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets", "templates")
    return template_dir