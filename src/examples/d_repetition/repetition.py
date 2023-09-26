def test_config():
    return True

def display_numbers(num):
   cnt = 0

   while cnt < num:
        print("cnt " + str(cnt) + " cnt + 1 " + str(cnt + 1) + " num " + str(num))
        cnt = cnt +1#a statement that makes the boolean expression false
        print("cnt after adding 1 " + str(cnt))

def sum_of_squares(num): #sum_of_squares(3) 1 * 1 +2 * 2 * 2 + # * 3 = 14
    sum = 0

    while num > 0:
        sum = sum + num * num
        num = num - 1

    return sum
       
def prompt_user():
    keep_going = 'y'

    while keep_going == 'y' or keep_going == 'Y':
        keep_going = input("Loop again, type y or Y: ")

def for_intro_loop():
    for num in [1,2,3,4,5]:
        print(num)

def for_intro_loop_strings():
    for lang in ["C++", "C#", "Java", "Python"]:
        print(lang)

def for_sum_of_squares(num):
    sum = 0

    for val in range(1, num+1):
        sum = sum + val * val

    return sum
    
def get_sum(num): #Loop to add count up until the count is equal or greater than num. 
    sum = 0
    cnt = 0

    while(cnt <= num):
        sum += cnt
        cnt += 1

    return sum

def get_sum_for(num):
    sum = 0

    for n in range(num):
        sum += n +1

    return sum

def for_num_range_w_start_value(num1, num2):

    for n in range(num1, num2):
        print(n)

def for_num_range_w_step_value(num1, num2, step):

    for n in range(num1, num2, step):
        print(n)

def for_display_squares(num1, num2):
    for n in range(num1, num2):
        square = n ** 2
        print(n, '\t', square)

def while_validate_user_input():
    lot_number = -1

    while(lot_number != 0):
        lot_number = input("Enter Lot Number (1-10) or 0 to exit ")
    
        if(lot_number.isnumeric()):
            lot_number = int(lot_number)

            if(lot_number !=0):
                while((lot_number < 1 or lot_number > 10)):
                    lot_number = int(input('Number must be in the range 1 to 10'))

            print("lot_number: " , lot_number)
        else:
            print("Exit")
    else:
        print("Lot number must be numeric")

def nested_while_loop(row, col):
    i = 0

    while(i < row):
        i += 1
        j = 0
        print("i:", i, "outer loop-wait for inner loop")

        while(j < col):
            print("j, ", j, "\t inner loop")
            j += 1

        print("inner loop complete")

def nested_for_loop(row, col):
    
    for i in range(row):
        print("i:", i , "outer loop")

        for j in range(col):
            print("j", j, "inner loop")

        print("inner loop complete")

def for_multiplication_table(row, col):

    for i in range(1, row+1):

        for j in range(1, col+1):

            print(str(i*j).rjust(3, " "), end =" ")

        print(" ")

def while_multiplication_table(row, col):

    i = 0

    while i < row:
        j = 0

        while j < col:
            product = (i + 1) * (j +1)
            print(str(product).rjust(3, " "), end= " ")

            j += 1

        i += 1
        print(" ")