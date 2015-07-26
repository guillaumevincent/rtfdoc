import os
import unittest

from rtfdoc.cmark import transform_markdown_into_html


class CmarkTestCase(unittest.TestCase):
    def test_convert_md_to_html(self):
        markdown_test_file = os.path.abspath(os.path.join("input", "test.md"))
        html = transform_markdown_into_html(markdown_test_file)
        expected_html = '<h1>title</h1>\n'
        self.assertEqual(expected_html, html)


if __name__ == '__main__':
    unittest.main()
