import random, time
from src.examples.j_classes.customer import Customer
from src.examples.j_classes.customer_data import CustomerData
from src.examples.j_classes.atm import ATM

def scan_card(customer_list_size):
    choice = input('Enter something...')#pause
    return random.randint(0, customer_list_size-1)

def display_menu():
    print('COSC Bank')
    print('1-Deposit')
    print('2-Withdraw')
    print('3-Display Balance')
    print('4-Exit')

def run_menu():
    random.seed(int(time.time()))
    customer_data = CustomerData ()
    list_customers = customer_data.get_customers();

    while(True):
        menu_choice = 0
        customer_index = scan_card(len(list_customers))
        
        customer = list_customers[customer_index]
        
        account_index = int(input("Enter 1 for checking 2 for savings"))

        account = customer.get_account(account_index-1)
        
        atm = ATM(account)

        while(menu_choice != '4'):
            display_menu()
            menu_choice = input("Enter choice: ")
            handle_menu(menu_choice, atm)

            if(menu_choice == '4'):
                customer_data.save_customers(list_customers)

def handle_menu(menu_choice, atm):

    if(menu_choice == '1'):
        atm.make_deposit()
    elif(menu_choice == '2'):
        atm.make_withdraw()
    elif(menu_choice == '3'):
        atm.display_balance()
    elif(menu_choice == '4'):
        print('Exiting...')
    else:
        print("invalid choice")
