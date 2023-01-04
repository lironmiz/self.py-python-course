# hangman project - unit five exercise.
# author - lirom mizrahi
'''
In the task at the end of the previous unit, you thoroughly dealt with cases wher
e the player types input that is not correct. Since the game "Hanged Man" includes
many guesses, the question arises: will we copy all these lines of code over and over
again for each guess? of course not.

That's why we will bundle part of the logic from the previous task as a function
called is_valid_input. The function is defined as:

def is_valid_input(letter_guessed):
Implement the is_valid_input function. The function receives as a parameter the string
letter_guessed, which represents the received character, and returns a Boolean value
representing whether the character is correct or not.

The function returns false (False, an invalid string) in the following cases:
If the letter_guessed string consists of two or more characters
If the string letter_guessed contains a sign that is not an English letter like: &, *)
The function returns true (True, a valid character) if the letter_guessed string
consists of only one letter that is an English letter (and not another character).
'''

def is_valid_input(letter_guessed):
    if letter_guessed == "E1" or letter_guessed == "E3" or letter_guessed == "E2":
        return False
    else:
        return True


def error_check(user_note):
    if len(user_note) > 1:
        if user_note.isalpha():
            return "E1"
        else:
            return "E3"
    elif len(user_note) == 1 and user_note.isalpha() != True:
        return "E2"
    else:
        return "fine"


def main():
    guess_a_letter = input("Guess a letter:")
    error = error_check(guess_a_letter)
    is_valid = is_valid_input(error)
    print(is_valid)


if __name__ == "__main__":
    main()
