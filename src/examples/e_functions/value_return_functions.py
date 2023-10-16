import random


def test_config():
    return True

def is_number_odd(num):
    return num % 2 == 1

def local_function_variable(val0):
    val = 100
    val2 = 10

global val3
val3 = 5

def global_variable_w_param(val3):
    val3 = 10

def global_variable():
    val3 = 10
    print(val3)

def global_variable_1():
    global val3
    val3 = 10
    print(val3)

def global_variable_2():
    print(val3)

def get_random_number(min, max):
    return random.randint(min, max)

def return_two_function_values(num1, num2):
    return num1, num2
