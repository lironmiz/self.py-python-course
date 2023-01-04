# hangman project - unit six part 2 exercise.
# author - lirom mizrahi
'''
In this exercise, you will act in accordance with the new letter that the player guessed:
either you will add it to the list of guesses, or you will print a message if it is not
possible to add it.

Write a function called try_update_letter_guessed defined as follows:

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
The function's acceptance values
A string called letter_guessed. The string represents the character received from the player.
A list called old_letters_guessed. The list contains the letters the player has guessed so far.

function operation
If the character is correct (ie one English letter) and has not been guessed before, the
function will add the letter_guessed character to the old_letters_guessed list. Then it will
return a true value (True) indicating that the addition was successful.
If the character is not correct (that is, it is not a single English letter) or it is already
in the list of guesses, the function will print the character X (the capital letter X) and below
it the list old_letters_guessed as a string of small letters that are sorted from small to large
and separated from each other by arrows (an arrow consists of the signs: <- , see sample output).
The printing of the organs is to remind the player which characters he has already guessed.
At the end, the function will return a false value (False), which means that it is not possible
to add the character to the list of already guessed characters.

directive
Use the check_valid_input function that you implemented in the previous exercise.

Examples of running the function

>>> old_letters = ['a', 'p', 'c', 'f']
>>> try_update_letter_guessed('A', old_letters)
X
a -> c -> f -> p
False
>>> try_update_letter_guessed('s', old_letters)
True
>>> old_letters
['a', 'p', 'c', 'f', 's']
>>> try_update_letter_guessed('$', old_letters)
X
a -> c -> f -> p -> s
False
>>> try_update_letter_guessed('d', old_letters)
True
>>> old_letters
['a', 'p', 'c', 'f', ‘s’, 'd']

'''

def error_check(user_note):
    if len(user_note) > 1:
        if user_note.isalpha():
            return "E1"
        else:
            return "E3"
    elif len(user_note) == 1 and user_note.isalpha() != True:
        return "E2"
    else:
        return user_note.lower()


def check_valid_input(letter_guessed, old_letters_guessed):
    if letter_guessed == "E1" or letter_guessed == "E3" or letter_guessed == "E2":
        return False
    else:
        if letter_guessed not in old_letters_guessed:
            old_letters_guessed = old_letters_guessed.append(letter_guessed)
            return True
        else:
            return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):

    letter_guessed = error_check(letter_guessed)
    if check_valid_input(letter_guessed, old_letters_guessed) == False:
        print('X')
        old_letters_guessed = ' -> '.join(sorted(old_letters_guessed))
        print(old_letters_guessed)
        return False
    else:
        return True

def main():

    old_letters = ['a', 'p', 'c', 'f']
    check_update = try_update_letter_guessed('A', old_letters)
    print(check_update)
    check_update = try_update_letter_guessed('s', old_letters)
    print(check_update)
    print(old_letters)
    check_update = try_update_letter_guessed('$', old_letters)
    print(check_update)
    check_update = try_update_letter_guessed('d', old_letters)
    print(check_update)
    print(old_letters)
    
if __name__ == "__main__":
    main()
