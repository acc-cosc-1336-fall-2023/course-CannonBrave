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