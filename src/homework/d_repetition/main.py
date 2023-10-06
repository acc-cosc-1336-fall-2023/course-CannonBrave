import repetition

while True:
    print("Homework 3 Menu")
    print("1. Factorial")
    print("2. Some odd numbers")
    print("3. Exit")
    choice = int(input('Enter a choice: '))
    
    if choice == 1:
        
        while True:
            num1 = int(input('Enter a number between 1 and 9: '))
            
            if num1 < 0 or num1 > 10:
                print('Error:')
            
            else:
                result = repetition.get_factorial(num1)
                print(result)
                break

    elif choice == 2:
        while True:
            num2 = int(input("Enter a number between 1 and 99: "))
            if num2 < 0 or num2 > 100:
                print('Error: ')
            else: 
                result = repetition.sum_odd_numbers(num2)
                print(result)
                break

    elif choice ==3:
        exit_choice = input('Do you want to continue (y/n)? ')
        if exit_choice == 'n':
            break
    

        

        




