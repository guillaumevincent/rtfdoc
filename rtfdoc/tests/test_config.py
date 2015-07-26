import os
import unittest

from rtfdoc.config import get_user_config


class ConfigTestCase(unittest.TestCase):
    def test_get_config(self):
        config_dir = os.path.abspath("config")
        config = get_user_config(config_dir)
        expected_config = {
            'root_dir': '.',
            'version': 'v1.0.0'
        }
        self.assertDictEqual(expected_config, config)

    def test_get_config_not_found(self):
        config = get_user_config('/tmp')
        self.assertEqual(1, config)

if __name__ == '__main__':
    unittest.main()
