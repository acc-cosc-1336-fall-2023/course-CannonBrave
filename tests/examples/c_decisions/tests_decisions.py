import unittest

from src.examples.c_decisions.decisions import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

