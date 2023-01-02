# hangman project - second unit exercise.
# author - lirom mizrahi
# In this exercise you will start developing the game by designing an "opening screen" that will
# appear to the player who starts playing. You need to create a designed "open screen"
# for the game.
# limit your gusses by using randint function
# Write a piece of code that prints to the screen the seven states of the hanging man, in order. The prints will be used by us in the advanced development stages of the game.
# Remember how you completed the previous exercise

# name of the game:
HANGMAN_ASCII_ART = print(""" _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/  |
                   |____ / """)

MAX_TRIES = random.randint(5,10)
print(MAX_TRIES)

guess_a_letter= input("Guess a letter:" )
guess_a_letter.lower()
print(guess_a_letter)

#images for the wrong gusses

#picture 1:
print("x-------x")
#picture 2:
print("""x-------x
|
|
|
|
|""")
#picture 3:
print("""x-------x
|       |
|       0
|
|
|""")
#picture 4:
print("""x-------x
|       |
|       0
|       |
|
|""")
#picture 5:
print("""x-------x
|       |
|       0
|      /|\\
|
|""")
#picture 6:
print("""x-------x
|       |
|       0
|      /|\\
|      /
|""")
#picture 7:
print("""x-------x
|       |
|       0
|      /|\\
|      / \\
|""")
