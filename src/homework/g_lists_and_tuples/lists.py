def get_p_distance(list1, list2):
    sum = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            sum += 1
    
    return sum / len(list1)

def get_p_distance_matrix(lists):
    n = len(lists)
    p_distance_matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(get_p_distance(lists[i], lists[j]))
        p_distance_matrix.append(row)
        
    return p_distance_matrix

def display_menu():
    print('1. Get p distance matrix')
    print('2. Exit')

def run_menu():
    menu_option = 0

    while(menu_option != '2'):
        display_menu()
        menu_option = input("Enter option: ")
        handle_menu_option(menu_option)

        if(menu_option == '2'):
            exit_option = input("Are you sure you want to exit? Type y/n: ")

            if(not(exit_option == "y" or exit_option == "Y")):
                menu_option = '0'

def handle_menu_option(menu_option):

    if(menu_option == '1'):
        dna_list_str = input('Enter a dna list formated as: [x,x,x,x], [x,x,x,x], n, ')
        stripped_str = dna_list_str.strip()[1:-1]
        outer_lists = stripped_str.split('], [')
    
        dna_list = []
        for outer_list in outer_lists:
            inner_list = outer_list.split(',')
            inner_list = [item.strip(" '") for item in inner_list]
            dna_list.append(inner_list)
              
        matrix = get_p_distance_matrix(dna_list)
        for row in matrix:
            print(' '.join([f'{val:.5f}' for val in row]))

    elif(menu_option == "2"):
        print("You typed exit...")

    else:
        print("Invalid option")
