import unittest

from src.examples.b_input_proc_output.input_process_output import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

