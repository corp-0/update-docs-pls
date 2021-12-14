import unittest
from update_docs_pls.config import Config
from update_docs_pls.exceptions import MissingConfigurationFile

class TestConfig(unittest.TestCase):
    def test_when_path_is_none_then_raise_exception(self):
        # Path can be None if the input environmental variable isn't set or wrote wrongly in action.yaml
        with self.assertRaises(MissingConfigurationFile):
            Config(None)

    def test_when_path_to_file_does_not_exists_raise_exception(self):
        with self.assertRaises(MissingConfigurationFile):
            Config('/path/to/file/that/does/not/exists')

    def test_when_file_exists_config_is_set(self):
        config = Config('data/test_config.yaml')
        self.assertIsNotNone(config)
        self.assertIsNotNone(config.entries)
        self.assertIsNotNone(config.entries)