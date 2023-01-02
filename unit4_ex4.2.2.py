# exercise 4.2.2 from unit 4
'''
Write a program that accepts a string
from the user and prints 'OK' if it is a palindrome, otherwise 'NOT'.

Guidelines
A palindrome is a string (word, number, or any sequence of characters) that is read from right to left the same as read from left to right. pay attention:
Uppercase or lowercase letters do not matter.
Ignore spaces.
Do not use loops.
'''

string = input("Enter a string: ")

# Remove spaces and make all characters lowercase
string = string.replace(" ", "").lower()

# Check if string is a palindrome
if string == string[::-1]:
  print("OK")
else:
  print("NOT")
