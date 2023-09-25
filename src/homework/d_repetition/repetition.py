def test_config():
    return True

def get_factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_odd_numbers(num):
    sum = 0
    i = 1

    while i <= num:
        if i % 2 != 0:
            sum += i
        i += 1
    return sum