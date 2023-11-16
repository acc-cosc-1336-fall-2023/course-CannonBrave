class ATM:
    #__bank_account = None

    def __init__(self, bank_account):
        self.__bank_account = bank_account

    def make_deposit(self):
        amount = int(input("Enter deposit amount: "))
        self.__bank_account.deposit(amount)

    def make_withdraw(self):
        amount = int(input("Enter withdraw amount: "))
        self.__bank_account.withdraw(amount)

    def display_balance(self):
        print(self.__bank_account.get_balance())
