import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget, get_inventory

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        add_inventory('Widget1', 10)
        self.assertEqual(get_inventory()['Widget1'], 10)
        
        add_inventory('Widget1', 25)
        self.assertEqual(get_inventory()['Widget1'], 35)

        add_inventory('Widget1', -10)
        self.assertEqual(get_inventory()['Widget1'], 25)

    def test_remove_inventory_widget(self):
        add_inventory('Widget1', 10)
        add_inventory('Widget2', 15)
        
        action = remove_inventory_widget('Widget1')
        self.assertEqual(action, 'Record deleted')
        self.assertEqual(len(get_inventory()), 1)
        self.assertTrue('Widget2' in get_inventory())

    def test_set_intersection(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        
        self.assertEqual(baseball.intersection(basketball), set(['Carmen', 'Alicia']))

    def test_set_union(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        
        self.assertEqual(baseball.union(basketball), set(['Jodi', 'Carmen', 'Aida', 'Alicia', 'Eva', 'Sarah']))

    def test_set_difference_baseball(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        
        self.assertEqual(baseball.difference(basketball), set(['Jodi', 'Aida']))

    def test_set_difference_basketball(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        
        self.assertEqual(basketball.difference(baseball), set(['Eva', 'Sarah']))
        self.assertEqual(baseball.difference(basketball), set(['Jodi', 'Aida']))

    def test_set_symetric_difference(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        
        self.assertEqual(basketball.symmetric_difference(baseball), set(['Jodi', 'Aida', 'Eva', 'Sarah']))
        
    