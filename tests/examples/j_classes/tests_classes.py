import unittest

from src.examples.j_classes.bank_account import BankAccount
from src.examples.j_classes.customer import Customer

class Test_Config(unittest.TestCase):

    def test_bank_account_balance(self):
        account = BankAccount(50)

        self.assertEqual(account.get_balance(), 50)

    def test_bank_account_deposit(self):
        #steps to get balance would happen here
        account = BankAccount(50)

        account.deposit(100)

        self.assertEqual(account.get_balance(), 150)
        
    def test_bank_account_deposit_negative_balance(self):
        account = BankAccount(50)

        account.deposit(-50)

        self.assertEqual(account.get_balance(), 50)

    def test_bank_account_withdraw(self):
        account = BankAccount(50)

        account.withdraw(20)

        self.assertEqual(account.get_balance(), 30)

    def test_bank_account_withdraw_negative_balance(self):
        account = BankAccount(50)

        account.withdraw(-10)

        self.assertEqual(account.get_balance(), 50)

    def test_bank_account_withdraw_more_than_balance(self):
        account = BankAccount(50)

        account.withdraw(51)

        self.assertEqual(account.get_balance(), 50)

    def test_bank_account_deposit_and_withdraw(self):
        account = BankAccount(50)

        account.deposit(100)
        self.assertEqual(account.get_balance(), 150)

        account.withdraw(20)
        self.assertEqual(account.get_balance(), 130)

    def test_bank_account_withdraw_and_deposit(self):
        account = BankAccount(50)

        account.withdraw(20)
        self.assertEqual(account.get_balance(), 30)

        account.deposit(100)
        self.assertEqual(account.get_balance(), 130)

    def test_bank_account_get_balance_from_db(self):
        account = BankAccount(-1)
        self.assertGreaterEqual(account.get_balance(), 0)
        self.assertLessEqual(account.get_balance(), 10000)

    def test_get_account_from_customer(self):
        customer = Customer(-1, -1)
        account = customer.get_account(0)
        print(account)
        self.assertGreaterEqual(account.get_balance(), 0)
        self.assertLessEqual(account.get_balance(), 10000)