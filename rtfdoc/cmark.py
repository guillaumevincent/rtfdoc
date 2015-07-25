import os
import fnmatch

import CommonMark


class Utils:
    def __init__(self):
        self.parser = CommonMark.DocParser()
        self.renderer = CommonMark.HTMLRenderer()

    def convert_md_to_html(self, markdown_file_path, input_dir, output_dir):
        markdown_relative_path = os.path.relpath(markdown_file_path, input_dir)
        html_relative_path = os.path.splitext(markdown_relative_path)[0] + '.html'

        html_file_path = os.path.join(output_dir, html_relative_path)

        if not os.path.exists(os.path.dirname(html_file_path)):
            os.makedirs(os.path.dirname(html_file_path))

        with open(markdown_file_path) as f, open(html_file_path, 'w') as w:
            parsed_markdown = self.parser.parse(f.read())
            html = self.renderer.render(parsed_markdown)
            w.write(html)

    def convert_dir_to_html(self, input_dir, output_dir):
        for root, dirnames, filenames in os.walk(input_dir):
            for filename in fnmatch.filter(filenames, '*.md'):
                self.convert_md_to_html(os.path.join(root, filename), input_dir, output_dir)
