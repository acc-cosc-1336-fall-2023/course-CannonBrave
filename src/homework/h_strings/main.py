import strings
#Prof - this code could be improved by:
    #3. allow for upper or lower case input y/n and DNA string
    #2 & 1 - verify that the dna string only consist of ATC & G
    #1 - verify that the two strings for Hamming distance are of equal length
while True:
    print("1. Hamming Distance")
    print("2. DNA Complement")
    print("3. Exit")
    choice = int(input('Enter a choice: '))

    if choice == 1:
        
        dna1 = input('Enter the first DNA string: ')
        dna2 = input('Enter the second DNA string: ')

        result = strings.get_hamming_distance(dna1, dna2)
        
        print('The hamming distance is: ' + str(result))

    elif choice == 2:
        
        dna = input('Enter DNA string for DNA complement: ')
        result = strings.get_dna_complement(dna)

        print('The DNA reverse complement is: ' + result)

    elif choice == 3:
        exit_choice = input('Do you want to continue (y/n)? ')
        if exit_choice == 'n':
            break
        