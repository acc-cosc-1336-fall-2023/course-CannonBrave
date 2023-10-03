def test_config():
    return True

def loop_string_w_while(str):
    indx = 0

    while indx < len(str):
        print(str[indx])
        indx += 1

def loop_string_w_for(str):

    for s_indx in range(0, len(str)):
        print(str[s_indx])

def loop_string_w_special_for(str):
    for ch in str:
        print(ch)