import sys
def welcome_Screen():
    """
    Print the logo and number of attempts.

    :param None
    :return: None
    :rtype: None
    """

    HANGMAN_GAME_LOGO = """
     __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.      _______      ___      .___  ___.  _______
    |  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |     /  _____|    /   \     |   \/   | |   ____|
    |  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |    |  |  __     /  ^  \    |  \  /  | |  |__
    |   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|
    |  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |    |  |__| |  /  _____  \  |  |  |  | |  |____
    |__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|     \______| /__/     \__\ |__|  |__| |_______|
                                                                                                                                   """
    print(HANGMAN_GAME_LOGO)
    MAX_TRIES = 6
    print(f"you have {MAX_TRIES} guess")

def choose_word(file_path, index):
    """
    the function return the secret word for guessing.

    :param file_path: A string representing a path to a text file containing space-separated words
    :param index: Position of a particular word in the file
    :return: the secret word for guessing
    :rtype: str
    """
    # open the file at read mode and read the words from the file
    while True:  # check if user file_path correct
        try:
            with open(file_path, 'r') as file:
                words = file.read().split()
            # take the secret word
            while True:  # check if user index is correct
                try:
                    secret_word = words[(int(index) - 1) % len(words)]
                    return secret_word
                except ValueError:
                    print(f"sorry, {index} is not a corret index. Please try again!")
                    sys.exit()

        except:
            print(f"sorry, {file_path} is not a corret file name. Please try again!")
            sys.exit()

def print_hangman(num_of_tries):
    """Prints the value of the key given as paramter.

    :param num_of_tries: a key for the dict(HANGMAN_PHOTOS)
    :type num_of_tries: int
    :return: None
    """

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
    |      /|\\
    |
    |""",
        6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",
        7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""
    }
    hangman_status = HANGMAN_PHOTOS[num_of_tries]
    print(hangman_status)

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    A Boolean function that accepts a character and a list of letters
    that the user has guessed previously. The function checks
    two things: the correctness of the input and whether it is legal
    to guess this letter (that is, the player has not guessed this letter before)
    and returns true or false accordingly.

    :param letter_guessed: character received from the user.
    :type letter_guessed: str
    :param old_letters_guessed: list contains the letters the player has guessed.
    :type old_letters_guessed: list
    :return: return True if it is a legal input, else return False
    :rtype: bool
    """
    # if the character is not valid return false
    if letter_guessed.isalpha() != True or len(letter_guessed) > 1:
        return False
    elif letter_guessed in old_letters_guessed: # if the character is not in the letters the player has guessed we return false
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    The method checks if the character is correct
    and if it is correct and does not exist in
    the letters that the user guessed then it updates the list with
    the new character and returns true otherwise it returns false

    :param letter_guessed: character received from the user.
    :type letter_guessed: str
    :param old_letters_guessed: list contains the letters the player has guessed.
    :type old_letters_guessed: list
    :return: return True if it is a legal input, else return False
    :rtype: bool
    """
    # check if the input is valid
    if check_valid_input(letter_guessed, old_letters_guessed) == False:
        print('X')
        old_letters_guessed = ' -> '.join(sorted(old_letters_guessed))
        print(old_letters_guessed)
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True

def show_hidden_word(secret_word, old_letters_guessed):
    """
    A function that returns a string consisting of letters and underscores.

    :param secret_word: word the user has to guess
    :type secret_word: str
    :param old_letters_guessed: list contains the letters the player has guessed.
    :type old_letters_guessed: str
    :return: reveal the secret word to the player in a lower-line structure
    :rtype: str
    """
    # we making the result string by loop all the letters in the secret word
    # and if the letter in the letters the user has guessed we add the letter to the result
    # and if not we and _ to the result
    result = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            result += letter + ' '
        else:
            result += '_ '
    return result

def check_win(secret_word, old_letters_guessed):
    """
    This is a boolean function that returns true if all the letters that make up the secret word
    are included in the list of letters that the user guessed. Otherwise, the function returns false.

    :param secret_word: word the user has to guess
    :param old_letters_guessed: list contains the letters the player has guessed.
    :type secret_word: str
    :type old_letters_guessed: list
    :return: true if all the letters that make up the secret word are included int the list of old_letters_guessed otherwise return false
    :rtype: bool
    """
    # looping all the letters in secret word if one of them not int the guessed word we return False otherwise we return True
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def main():

    # print the welcome screen
    welcome_Screen()
    wrong_guess = 0
    num_of_tries = 1
    old_letters_guessed = list()  # create an empty list for the beginning
    # take from user the file path and index
    file_path = input("Enter file path: ")
    index = input("Enter index: ")
    secret_word = choose_word(file_path, index)
    print("Let’s start!")
    print_hangman(num_of_tries)
    print("_ " * len(secret_word))
    # game loop
    while wrong_guess in range(6):
        # take user input
        guessed_letter = input("Guess a letter: ").lower()
        # the main logic of the game
        if try_update_letter_guessed(guessed_letter, old_letters_guessed):
            if guessed_letter not in secret_word:
                wrong_guess += 1
                num_of_tries += 1
                print(":(")
                print_hangman(num_of_tries)
                print(show_hidden_word(secret_word, old_letters_guessed))
            else:
                print(show_hidden_word(secret_word, old_letters_guessed))
                if check_win(secret_word, old_letters_guessed):
                    print("WIN")
                    break
    if wrong_guess == 6:
        if check_win(secret_word, old_letters_guessed):
            print("WIN")
        else:
            print("LOSE")

if __name__ == "__main__":
    main()