# exercise 3.4.3 from unit 3
'''
Write a program that accepts a string of his choice from the user.
The program prints the string where the letters in the first half of the string are lowercase, and the letters in the second half of the string are uppercase.
If the length of the string is odd, the first half will be one less than the second half.

An example of running the program
Please enter a string: astronaut
astrONAUT

Guidelines
Do not use loops or if condition statement.
Use slicing on strings.
Assume that the length of the string is greater than 2.
'''

str = input("Please enter a string: ")

# calculate the length of the first half
first_half_len = len(str) // 2

# make the first half lowercase
first_half = str[:first_half_len].lower()

# make second half of the string in uppercase 
second_half = str[first_half_length:].upper()

output = first_half + second_half

print(output)
