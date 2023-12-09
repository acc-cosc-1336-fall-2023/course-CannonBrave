from src.examples.j_classes.customer import Customer

class CustomerData:

    __file_name = 'customers.dat'

    def save_customers(self, customer_list):
        
        out_file = open(self.__file_name, 'w')

        for customer in customer_list:
            out_file.write(str(customer.get_account(0).get_balance()) + ',' + str(customer.get_account(1).get_balance()) + '\n')

        out_file.close();

    def get_customers(self):
        in_file = open(self.__file_name, 'r')
        checking_balance = 0
        savings_balance = 0
        list_customers = []

        for line in in_file:
            balances = line.rstrip('\n').split(',')
            checking_balance = int(balances[0])
            savings_balance = int(balances[1])

            customer = Customer(checking_balance, savings_balance)
            list_customers.append(customer)

        in_file.close()

        return list_customers