import os
import shutil
import unittest

from rtfdoc.cmark import Utils


class CmarkTestCase(unittest.TestCase):
    def test_convert_md_to_html(self):
        utils = Utils()
        input_dir = os.path.abspath("input")
        output_dir = os.path.abspath("output")
        markdown_test_file = os.path.join(input_dir, "a.md")
        utils.convert_md_to_html(markdown_test_file, input_dir, output_dir)
        self.assertTrue(os.path.exists(output_dir))
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'a.html')))
        shutil.rmtree(output_dir)

    def test_convert_dir(self):
        utils = Utils()
        input_dir = os.path.abspath("input")
        output_dir = os.path.abspath("output")
        utils.convert_dir_to_html(input_dir, output_dir)
        self.assertTrue(os.path.exists(output_dir))
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'a.html')))
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'dir', 'b.html')))
        shutil.rmtree(output_dir)


if __name__ == '__main__':
    unittest.main()
