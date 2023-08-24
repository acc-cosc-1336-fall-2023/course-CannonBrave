import unittest

from src.examples.f_files_exception.exceptions import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

