import decisions

result = decisions.is_overtime(40)

if(result == False):
    print('40 is not overtime')


if(result):
    print('Is overtime')
else:
    print("Not overtime")
