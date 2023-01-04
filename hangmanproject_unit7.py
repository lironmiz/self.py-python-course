# hangman project - unit seven part 1 and 2 exercise.
# author - lirom mizrahi
'''
7.3.1
In this exercise you will show the player his progress in guessing the secret word.

Write a function called show_hidden_word defined as follows:

def show_hidden_word(secret_word, old_letters_guessed):
The function's acceptance values
A string called secret_word. The string represents the secret word that the player has to guess.
A list called old_letters_guessed. The list contains the letters the player has guessed so far.
The return values of the function
The function returns a string consisting of letters and underscores. The string shows the
letters from the old_letters_guessed list that are in the secret_word string in their
appropriate position, and the other letters in the string (which the player has not yet guessed)
as underlines.

Example of running the show_hidden_word function:

>>> secret_word = "mammals"
>>> old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
>>> print(show_hidden_word(secret_word, old_letters_guessed))
m _ m m _ _ s
Guidelines
To make it clear to the player how many letters are left to guess, space the string
when you print the underscores

7.3.2
Time to check if the player has already won, right?
In this exercise you will write a function that checks whether the player was able to guess the secret word and thus won the game!

Write a function called check_win defined as follows:

def check_win(secret_word, old_letters_guessed):
The function's acceptance values
A string called secret_word. The string represents the secret word that the player has to guess.
A list called old_letters_guessed. The list contains the letters the player has guessed so far.
The return values of the function
The function returns true if all the letters that make up the secret word are included in the list of letters that the user guessed. Otherwise, the function returns false.

Examples of running the check_win function
>>> secret_word = "friends"
>>> old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
>>> print(check_win(secret_word, old_letters_guessed))
False
>>> secret_word = "yes"
>>> old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
>>> print(check_win(secret_word, old_letters_guessed))
True

'''

def show_hidden_word(secret_word, old_letters_guessed):
    result = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            result += letter + ' '
        else:
            result += '_ '
    return result.strip()

def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def main():
    secret_word = "lironrrrg"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'l', 'r']
    print(show_hidden_word(secret_word, old_letters_guessed))
    secret_word = "friends"
    old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    print(check_win(secret_word, old_letters_guessed))
    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word, old_letters_guessed))
if __name__ == "__main__":
    main()

