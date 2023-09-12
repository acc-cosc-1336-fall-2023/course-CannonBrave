import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
from tests.homework.b_in_proc_out import tests_in_proc_out
    #homework 1
#from tests.examples.c_decisions import tests_decisions
    #class
#from tests.homework.c_decisions import tests_decisions
    #homework 2

#suite = unittest.TestLoader().loadTestsFromModule(test_decisions)
    #homework 1
suite = unittest.TestLoader().loadTestsFromModule(tests_in_proc_out)
    #homework 2
    
unittest.TextTestRunner(verbosity=2).run(suite)