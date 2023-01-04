# exercise 7.2.2 from unit 7
'''
Write a function called numbers_letters_count defined as follows:

def numbers_letters_count(my_str):
The function accepts as a string parameter.
The function returns a list in which the first member represents the number of digits in the string, and the second member represents the number of letters in the string, including spaces, periods, punctuation marks, and anything other than digits.

An example of running the numbers_letters_count function:
>>> print(numbers_letters_count("Python 3.6.3"))
[3, 9]
'''

def numbers_letters_count(my_str):
    digits = 0
    letters = 0
    for ch in my_str:
        if ch.isdigit():
            digits += 1
        else:
            letters += 1
    return [digits, letters]

def main():
    print(numbers_letters_count("Python 3.6.3")) 
    print(numbers_letters_count("Hello liron")) 

if __name__ == "__main__":
    main()
