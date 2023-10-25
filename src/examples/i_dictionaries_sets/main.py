#main program
#phonebook = {'Chris':'555-1111', 'Katie':'555-222', 'Joanne':'555-3333'}
#print(phonebook)

#print(phonebook['Chris'])
#print(phonebook['Katie'])

#for key in phonebook:
#    print(key, phonebook[key])

#print('Values only')
#for value in phonebook.values():
#        print(value)

#print('dictionary items')
#for item in phonebook.items():
#    print(item)

#exists = dictionary.is_key_in_dictionary('Chris', phonebook)

#print(exists)

import dictionaries
import sets

#main program
phonebook = {}#empty dictionary

'''key = input("Enter key: ")
value = input("Enter value: ")

phonebook[key] = value

print(phonebook)

key = input("Enter key: ")
value = input("Enter value: ")

phonebook[key] = value

print(phonebook)'''

'''dictionaries.add_friend_phonebook('Chris', '555-1111', phonebook)
dictionaries.add_friend_phonebook('Katie', '555-1111', phonebook)

for name, value in phonebook.items():
    print(name, value)

print('\nUpdate Katie |n')
dictionaries.update_friend_phonebook('Katie', '555-2345', phonebook)

for name, value in phonebook.items():
    print(name, value)

print('\nDelete Chris \n')
dictionaries.delete_friend_phonebook('Chris', phonebook)
for name, value in phonebook.items():
    print(name, value)'''

myset = set('abc')

print (myset)

myset.add('d')

print(myset)

for item in myset:
    print(item)

