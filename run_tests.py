import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
from tests.homework.b_in_proc_out import tests_in_proc_out

suite = unittest.TestLoader().loadTestsFromModule(tests_in_proc_out)
unittest.TextTestRunner(verbosity=2).run(suite)
