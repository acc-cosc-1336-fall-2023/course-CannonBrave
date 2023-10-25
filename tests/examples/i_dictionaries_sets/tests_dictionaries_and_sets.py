import unittest

from src.examples.i_dictionaries_sets.dictionaries import add_friend_phonebook, delete_friend_phonebook, is_key_in_dictionary, test_config, update_friend_phonebook

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_is_key_in_dictionary(self):
        phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

        self.assertEqual(is_key_in_dictionary('Cris', phonebook), False)
        self.assertEqual(is_key_in_dictionary('Chris', phonebook), True)

    def test_add_friend_phonebook(self):
        phonebook = {}
        add_friend_phonebook('Chris', '555-1111', phonebook)
        
        self.assertEqual(phonebook, {'Chris':'555-1111'})
    
    def test_update_friend_phonebook(self):
        phonebook = {'Chris':'555-1111'}

        update_friend_phonebook('Chris', '555-1234', phonebook)
        self.assertEqual(phonebook, {'Chris':'555-1234'})

        update_friend_phonebook('Cris', '555-4321', phonebook)
        self.assertEqual(phonebook, {'Chris':'555-1234'})

    def test_delete_friend_phonebook(self):
        phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        delete_friend_phonebook('Chris', phonebook)

        self.assertEqual(phonebook, {'Katie':'555-2222', 'Joanne':'555-3333'})

        delete_friend_phonebook('Kati', phonebook)
        self.assertEqual(phonebook, {'Katie':'555-2222', 'Joanne':'555-3333'})