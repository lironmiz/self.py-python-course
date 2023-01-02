# hangman project - three unit exercise.
# author - lirom mizrahi
'''
3.5.1
In the unfolding task at the end of the previous unit, you began to realize
the basis of the game. You have captured a character guess from the user and 
printed it to the screen.

Since the size of the letters that are guessed in the game is not important
(ie, lowercase or uppercase), you must change the piece of code you wrote
so that the guessed letter is always displayed on the screen as a lowercase letter.

3.5.2
In the previous exercise, you implemented a short program that asks
the player to guess a letter, but you have not yet shown him the word pattern
for which he must guess letters, that is, the number of letters that make up the secret word.

It's time to create the "game board" for the player, that is, the sequence of
underscores that mark the position of the missing letters in the word to be guessed.

Write a piece of code according to the following sections:

Accept a one-word string (without spaces) from the user.
Print a new string that will contain multiple underscores spaced next to each other, the length of the received string.

Guidelines
Solve the section without using loops.
Ensure accurate output.

'''
# 3.5.1
guess_letter= input("Guess a letter:" )
print(guess_letter.lower())

# 3.5.2
# compute the length of the word
word = input("Please enter a word: ")
word_len = len(word)
output = "_ " * word_len

# print an the empty _ based on the length of the word
print(output)
