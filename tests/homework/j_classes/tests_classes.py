import unittest

from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):

    def test_get_roll_value(self):
        for _ in range(3):
            die = Die()
            die.roll()
            number_rolled = die.get_rolled_value()
            self.assertTrue(1 <= number_rolled <= 6)

    
