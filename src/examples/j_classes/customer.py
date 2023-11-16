import src.examples.j_classes.bank_account

class Customer:

    __list_accounts = []

    def __init__(self):
        self.__list_accounts.append(src.examples.j_classes.bank_account.BankAccount(-1))#add one account to the list
        self.__list_accounts.append(src.examples.j_classes.bank_account.BankAccount(-1))#add one account to the list

    def get_account(self, index):
        return self.__list_accounts[index]