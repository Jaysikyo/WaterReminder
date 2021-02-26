"""
Unit Testing for the Config class.

:author: Jacob Singleton
"""


import unittest
from config import Config
from pathlib import Path


class ConfigTest(unittest.TestCase):
    def test_loading_yaml_data(self):
        yaml_data: dict = Config.get_yaml_data(Path('test/dummy_config_data.yml'))

        self.assertEqual(yaml_data, {'first': '1', 'second': 'third', 'fourth': '50', 'fifth': 'sixth'})

    def test_loading_all_correct_config_values(self):
        config = Config(Path('test/dummy_config_correct.yml'))

        self.assertEqual(config.audio_path, 'audio/')

        self.assertEqual(config.min_interval, 600)
        self.assertEqual(config.max_interval, 900)

    def test_loading_all_incorrect_config_values_sets_them_to_default(self):
        config = Config(Path('test/dummy_config_incorrect.yml'))

        self.assertEqual(config.min_interval, 60)
        self.assertEqual(config.max_interval, 90)

    def test_loading_single_correct_config_string(self):
        config = Config(Path('test/dummy_config.yml'))
        yaml_data = Config.get_yaml_data(Path('test/dummy_config.yml'))

        config.load_variable(yaml_data, 'extra-string', 'extra_string', str, 'invalid')

        self.assertTrue('extra_string' in config.__dict__)
        self.assertEqual(config.__dict__['extra_string'], 'hello!')

    def test_loading_single_correct_config_integer(self):
        config = Config(Path('test/dummy_config.yml'))
        yaml_data = Config.get_yaml_data(Path('test/dummy_config.yml'))

        config.load_variable(yaml_data, 'extra-integer', 'extra_integer', int, 0)

        self.assertTrue('extra_integer' in config.__dict__)
        self.assertEqual(config.__dict__['extra_integer'], 10)

    def test_loading_single_incorrect_config_string_loads_default_value(self):
        config = Config(Path('test/dummy_config_correct.yml'))
        yaml_data = Config.get_yaml_data(Path('test/dummy_config_correct.yml'))

        config.load_variable(yaml_data, 'extra-string', 'extra_string', str, 'invalid')

        self.assertTrue('extra_string' in config.__dict__)
        self.assertEqual(config.__dict__['extra_string'], 'invalid')

    def test_loading_single_incorrect_integer_string_loads_default_value(self):
        config = Config(Path('test/dummy_config_correct.yml'))
        yaml_data = Config.get_yaml_data(Path('test/dummy_config_correct.yml'))

        config.load_variable(yaml_data, 'extra-integer', 'extra_integer', int, 100)

        self.assertTrue('extra_integer' in config.__dict__)
        self.assertEqual(config.__dict__['extra_integer'], 100)

    def test_loading_default_config_values(self):
        config = Config(Path('test/dummy_config_correct.yml'))

        config.load_defaults()

        self.assertEqual(config.audio_path, 'reminder-audio/')

        self.assertEqual(config.min_interval, 60)
        self.assertEqual(config.max_interval, 90)


if __name__ == '__main__':
    unittest.main()
