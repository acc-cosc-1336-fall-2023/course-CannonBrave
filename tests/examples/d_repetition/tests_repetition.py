import unittest

from src.examples.d_repetition.repetition import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

