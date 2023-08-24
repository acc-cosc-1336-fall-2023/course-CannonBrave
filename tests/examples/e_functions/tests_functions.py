import unittest

from src.examples.e_functions.value_return_functions import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

