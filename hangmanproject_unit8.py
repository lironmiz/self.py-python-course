# hangman project - unit 8 exercise 
# author - lirom mizrahi
'''
Towards the end of the development of the game "Hanged Man" we had to go back and print each time one of the status images of the hanging man, depending on the number of wrong guesses the player guessed.

For this purpose, follow the following instructions:

Define a constant variable called HANGMAN_PHOTOS. The variable is of dictionary type (dict) and must hold the seven states of the hanging man (which you encountered in the unfolding task at the end of Unit 1).
Write a function called print_hangman defined as follows:
def print_hangman(num_of_tries):
The function prints one of the seven states of the hanging man, using:
A variable called num_of_tries that represents the number of failed attempts by the user so far.
The HANGMAN_PHOTOS variable you defined.
An example of running the print_hangman function
>>> num_of_tries = 6
>>> print_hangman(num_of_tries)
x-------x
| |
| 0
| /|\
| / \
|
'''
def print_hangman(num_of_tries):
   HANGMAN_PHOTOS = {
        1: """    x-------x""",
        2: """    x-------x
    |
    |
    |
    |
    |""",
        3: """    x-------x
    |       |
    |       0
    |
    |
    |""",
        4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""",
        5: """    x-------x
    |       |
    |       0
    |      /|\
    |
    |""",
        6: """    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |""",
        7: '''    x-------x
    |       |
    |       0
    |      /|
    |      / 
    |'''
    }
   if num_of_tries in HANGMAN_PHOTOS.keys():
     print(HANGMAN_PHOTOS[num_of_tries])
   else:
     print('X')

print(print_hangman(7))
