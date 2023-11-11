import bank_account, atm, menu

account = bank_account.BankAccount(50)
my_atm = atm.ATM(account)

menu.run_menu(my_atm)
