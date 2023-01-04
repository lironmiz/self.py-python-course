# hangman project - unit six part 1 exercise.
# author - lirom mizrahi
'''
To remind you, in the unfolding task at the end of the previous unit, you wrote a function to check the correctness 
of input from the user. In this exercise, you will upgrade the function so that it also refers to the letters that
the player has already guessed in the game in the tests.

Write the function, this time call it check_valid_input, and define it as follows:

def check_valid_input(letter_guessed, old_letters_guessed):
Acceptance values of the function:
A string called letter_guessed. The string represents the character received from the player.
A list called old_letters_guessed. The list contains the letters the player has guessed so far.
The return values of the function
The function returns a Boolean value representing the correctness of the string and whether the user has already guessed the character before.

The function returns false (False, an invalid string) in the following cases:
If the letter_guessed string consists of two or more characters
If the string letter_guessed contains a sign that is not an English letter (like: &, *)
If the letter_guessed string is a character already in the old_letters_guessed list (that is, this character has
been guessed before and therefore it is illegal to guess it again)
The function returns true (True, a valid character) if the string letter_guessed consists of only one letter
that is an English letter (and not another sign) that is not in the list old_letters_guessed

Examples of running the check_valid_input function

>>> old_letters = ['a', 'b', 'c']
>>> check_valid_input('C', old_letters)
False
>>> check_valid_input('ep', old_letters)
False
>>> check_valid_input('$', old_letters)
False
>>> check_valid_input('s', old_letters)
True

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


def main():
    guess_a_letter = input("Guess a letter:")
    letter_guessed = error_check(guess_a_letter)
    check_valid = check_valid_input(letter_guessed, old_letters_guessed=['a', 'b', 'c'])
    print(check_valid)

if __name__ == "__main__":
    main()
