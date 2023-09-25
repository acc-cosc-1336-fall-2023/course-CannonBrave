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
from tests.homework.d_repetition import tests_repetition

#suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)
    #class examples / Homework 1
#suite = unittest.TestLoader().loadTestsFromModule(tests_in_proc_out)
    #homework 2
suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
unittest.TextTestRunner(verbosity=2).run(suite)                       