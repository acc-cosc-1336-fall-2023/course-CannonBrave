import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.homework.b_in_proc_out import tests_in_proc_out
    #homework 1
#from tests.examples.c_decisions import tests_decisions
    #class examples
#from tests.homework.c_decisions import tests_decisions
    #homework 2
#from tests.examples.d_repetition import tests_repetition 
    #class examples
#from tests.homework.d_repetition import tests_repetition
#from tests.examples.e_functions import tests_functions
#from tests.homework.e_functions import tests_functions
#from tests.examples.h_strings import tests_strings
#from tests.homework.h_strings import tests_strings
#from tests.examples.g_lists_and_tuples import tests_lists_and_tuples
#from tests.examples.i_dictionaries_sets import tests_dictionaries_and_sets
#from tests.homework.i_dictionaries_sets import tests_dictionaries_and_sets
from tests.homework.j_classes import tests_classes
#suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)
    #class examples / Homework 1
#suite = unittest.TestLoader().loadTestsFromModule(tests_in_proc_out)
    #homework 2
suite = unittest.TestLoader().loadTestsFromModule(tests_classes)
unittest.TextTestRunner(verbosity=2).run(suite)
