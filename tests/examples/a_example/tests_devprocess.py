import unittest

from src.examples.a_example.devprocess import add_numbers
from src.examples.a_example.devprocess import echo_number

class Test_Config(unittest.TestCase):

    def test_add_numbers_2(self):
        self.assertEqual(2, add_numbers(1, 1))

    def test_add_numbers_100(self):
        self.assertEqual(100, add_numbers(50, 50))

    def test_add_numbers_200(self):
        self.assertEqual(200, add_numbers(50, 150))

    def test_echo_number_5(self):
        self.assertEqual(5, echo_number(5))

    def test_echo_number_500(self):
        self.assertEqual(500, echo_number(500))

    def test_echo_number_5000(self):
        self.assertEqual(5000, echo_number(5000))