import src.examples.j_classes.bank_account

class Customer:

    def __init__(self, checking_balance, saving_balance):
        self.__list_accounts = []
        checking_account = src.examples.j_classes.bank_account.BankAccount(checking_balance)
        savings_account = src.examples.j_classes.bank_account.BankAccount(saving_balance)
        self.__list_accounts.append(checking_account)#add one account to the list
        self.__list_accounts.append(savings_account)#add one account to the list

    def get_account(self, index):
        return self.__list_accounts[index]