class BankAccount:
    __balance = 0 #hide it from other classes

    def __init__(self, balance):#constructor --initialize class data/variables
        self.__balance = balance

    def get_balance(self):#other classes can see get_balance
        return self.__balance

    def deposit(self, amount):

        if(amount > 0):
            self.__balance += amount

    def withdraw(self, amount):

        if(amount > 0 and amount <= self.__balance):
            self.__balance -= amount
