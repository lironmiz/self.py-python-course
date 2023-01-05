# hangman project - unit 9 exercise.
# author - lirom mizrahi
'''
This task will choose for the player a word that will be the secret word for the guess,
from a text file containing a list of words separated by spaces.

Write a function called choose_word defined as follows:

def choose_word(file_path, index):
The function accepts as parameters:

A string (file_path) representing a path to the text file.
An integer (index) representing the position of a certain word in the file.
The function returns a tuple consisting of two members in the following order:

The number of different words in the file, i.e. not including repeated words.
A word in the position received as an argument to the function (index), which will be used as the secret word for guessing.
Guidelines
Treat the positions the player enters as starting from 1 (rather than zero).
If the position (index) is greater than the number of words in the file, the function
continues to count positions in a circular fashion (that is, returns to the first position
in the original list of words in the file and God forbid).
An example of a text file that contains a list of words, called words.txt
hangman song most broadly is a song hangman work music work broadly is typically
Examples of running the choose_word function with the words.txt file
>>> choose_word(r"c:\words.txt", 3)
(9, 'most')
>>> choose_word(r"c:\words.txt", 15)
(9, 'hangman')

'''

def choose_word(file_path, index):
    with open(file_path, 'r') as f:
        words = f.read().split()

    num_unique_words = len(set(words))

    secret_word = words[(index - 1) % len(words)]

    return (num_unique_words, secret_word)

def main():
    result = choose_word(r"words.txt", 3)
    print(result)
    result = choose_word(r"words.txt", 15)
    print(result)

if __name__ == "__main__":
    main()
