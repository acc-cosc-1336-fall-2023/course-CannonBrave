import unittest

from src.examples.c_decisions.decisions import get_and_result, get_letter_grade, get_notted_value, get_or_result, is_consonant, is_even, is_odd, is_overtime, is_vowel, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_and_truth_table(self):
        self.assertEqual(True, get_and_result(True, True))
        self.assertEqual(False, get_and_result(True, False))
        self.assertEqual(False, get_and_result(False, True))
        self.assertEqual(False, get_and_result(False, False))

    def test_or_truth_table(self):
        self.assertEqual(True, get_or_result(True, True))
        self.assertEqual(True, get_or_result(True, False))
        self.assertEqual(True, get_or_result(False, True))
        self.assertEqual(False, get_or_result(False, False))

    def test_not_truth_table(self):
        self.assertEqual(True, get_notted_value(False))
        self.assertEqual(False, get_notted_value(True))

    def test_is_even(self):
        self.assertEqual(False, is_even(1))
        self.assertEqual(True, is_even(2))
        self.assertEqual(False, is_even(101))

    def test_is_odd(self):
        self.assertEqual(True, is_odd(1))
        self.assertEqual(False, is_odd(2))
        self.assertEqual(True, is_odd(101))
        self.assertEqual(False, is_odd(102))

    def test_is_vowel(self):
        self.assertEqual(True, is_vowel('a'))
        self.assertEqual(True, is_vowel('e'))
        self.assertEqual(True, is_vowel('i'))
        self.assertEqual(True, is_vowel('o'))
        self.assertEqual(True, is_vowel('u'))

    def test_is_consonant(self):
        self.assertEqual(False, is_consonant('a'))
        self.assertEqual(True, is_consonant('b'))

    def test_is_overtime(self):
        self.assertEqual(False, is_overtime(30))
        self.assertEqual(True, is_overtime(41))

    def test_get_letter_grade(self):
        self.assertEqual(get_letter_grade(105), "Invalid Grade")
        self.assertEqual(get_letter_grade(100), "A")
        self.assertEqual(get_letter_grade(95), "A")
        self.assertEqual(get_letter_grade(90), "A")
        self.assertEqual(get_letter_grade(85), "B")
        self.assertEqual(get_letter_grade(75), "C")
        self.assertEqual(get_letter_grade(65), "D")
        self.assertEqual(get_letter_grade(55), "F")
        self.assertEqual(get_letter_grade(-5), "Invalid Grade")