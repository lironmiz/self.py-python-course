# exercise 5.3.4 from unit 5
'''
The function accepts as a string parameter. The function returns true if the last character that appears in the string also appears before. Otherwise the function returns false.

Guidelines
Uppercase or lowercase letters are not important.
'''

def last_early(my_str):
    my_str = my_str.lower()

    last_char = my_str[-1]

    return last_char in my_str[:-1]

print(last_early("happy birthday")) # True

print(last_early("best of luck")) # False

print(last_early("Wow")) # True

print(last_early("X")) # False



  
