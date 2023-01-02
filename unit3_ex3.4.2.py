# exercise 3.4.2 from unit main
'''
Write a program that accepts a string of his choice from the user.
The program will print to the screen a string in which all occurrences
of the first character have been replaced by the character 'e', except for the first
character itself.

example: 
Please enter a string: ddar astronaut. pldase, stop drasing md!
dear astronaut. please, stop erasing me!

'''

str = input("Enter a string: ")
char_to_replace = str[0]
if(len(str) > 1):
  output = str[0] + str[1:].replace(char_to_replace, 'e')
else:
  output = str[0]
  
print(output)

