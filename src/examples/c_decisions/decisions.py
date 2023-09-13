def test_config():
    return True

def get_and_result(bool1, bool2):
    result = bool1 and bool2
    return result

def get_or_result(bool1, bool2):
    result = bool1 or bool2
    return result

def get_notted_value(bool1):
    return not bool1

def is_even(num1):
    result = num1 % 2 == 0
    return result

def is_odd(num1):
    result = num1 % 2 == 1 #is the remainder of num / 2 equal to zero
    return result

def is_vowel(letter):
    result = letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'
    return result

def is_consonant(letter):
    result = letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u'
    return result

def is_overtime(hours):
    result = False
    result = hours > 40
    return result

def get_letter_grade(grade):
    letter_grade = ""

    if(grade >= 90 and grade <= 100):
        letter_grade = "A"
    elif(grade >= 80 and grade < 90):
        letter_grade = "B"
    elif(grade >= 70 and grade < 80):
        letter_grade = "C"
    elif(grade >= 60 and grade < 70):
        letter_grade = "D"
    elif(grade >= 0 and grade < 60):
        letter_grade = "F"
    else:
        letter_grade = "Invalid Grade"

    return letter_grade
        