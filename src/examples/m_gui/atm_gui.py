import tkinter
import tkinter.messagebox
import bank_account

class ATM_GUI:

    def __init__(self):
        self.__atm_gui = tkinter.Tk()
        self.__account = bank_account.BankAccount(-1)

        self.__amount_entry = tkinter.Entry(self.__atm_gui, width=10)
        self.__amount_entry.pack()

        self.__label = tkinter.Label(self.__atm_gui, text = 'Balance: ' + str(self.__account.get_balance()))
        self.__label.pack()                             

        self.__deposit_button = tkinter.Button(self.__atm_gui, text ='Deposit', command=self.deposit)
        self.__deposit_button.pack()

        self.__withdrawal_button = tkinter.Button(self.__atm_gui, text ='Withdraw', command=self.withdraw)
        self.__withdrawal_button.pack()

        self.__atm_gui.mainloop()

    def deposit(self):
        self.__account.deposit(int(self.__amount_entry.get()))
        self.__label['text'] = 'Balance: ' + str(self.__account.get_balance())

    def withdraw(self):
        self.__account.withdraw(int(self.__amount_entry.get()))
        self.__label['text'] = 'Balance: ' + str(self.__account.get_balance())