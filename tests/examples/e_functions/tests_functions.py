import unittest

from src.examples.e_functions.value_return_functions import get_random_number, local_function_variable, return_two_function_values, test_config
val3 = 5

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_local_function_variable(self):
        val = 0
        local_function_variable(val)

        self.assertEqual(val, 0)

    def test_get_random_number(self):
        rand = get_random_number(1, 100)
        is_number_in_range = rand >= 1 and rand <= 100

        self.assertEqual(is_number_in_range, True)

    def test_return_two_function_values(self):
        num1,num2 = return_two_function_values(4,5)
        
        self.assertEqual(num1, 4)
        self.assertEqual(num2, 5)