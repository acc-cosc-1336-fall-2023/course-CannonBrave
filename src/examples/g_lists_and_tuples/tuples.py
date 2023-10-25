#
def create_tuple():
    num = (1,2,3,4,5)#tuple
    print(num)

    for i in num:
        print(i)

    for i in range(0, len(num)):
        print(num[i])

def create_list_from_tuple():
    nums = (1,2,3,4,5)#tuple
    nums_list = list(nums)

    print(nums_list)