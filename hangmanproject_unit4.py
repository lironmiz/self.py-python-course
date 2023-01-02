# hangman project - unit four exercise.
# author - lirom mizrahi
'''
Remember the unfolding task at the end of the previous unit,
where we received a guess from the player? Have you ever wondered what happens if the
player accidentally types a character that is not an English letter? Or more than one died?
When we ask for input from the user, we must assume that the input will not necessarily
be correct and therefore it is our responsibility to perform correctness checks on it.

In this exercise you must receive a note from the user (the player).
Depending on the received character, print a message to the screen regarding its correctness,
according to the following requirements:

For an invalid character:
If the player entered a string of letters with more than one letter,
print the string "E1" to the screen.
If the player entered a character that is not an English letter
(for example a sign like: &, *), print the string "E2" to the screen.
If the player entered a letter string that has more than one character and also
contains non-English characters, print the string "E3" to the screen.

For a valid character:
If the received character is one character and also an English letter
(and not another character), print it to the screen as a lowercase letter.

'''

note = input("Enter a note: ")

if not note.isalpha() or len(note) > 1:
  # Check if string contains non-alphabetic characters or has more than one character
  if not note.isalpha():
    print("E3")
  else:
    print("E1")
else:
  # Print lowercase version of the letter
  print(note.lower())
