# exersice 7.2.7 from unit 7
'''
Write a function called arrow defined as follows:

def arrow(my_char, max_length):
The function accepts two parameters: the first is a single character, the second is a maximum size.
The function returns a string representing an "arrow" structure (see example), built from the input, where the center of the arrow (the longest line) is the length of the size passed as a parameter.

An example of running the arrow function
print(arrow('*', 5))
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

def arrow(my_char, max_length):
    arrow_str = ''
    for i in range(max_length):
        arrow_str += (my_char + ' ') * i + my_char + '\n'
    for i in range(max_length - 2, -1, -1):
        arrow_str += (my_char + ' ') * i + my_char + '\n'
    return arrow_str

def main():
    print(arrow('*', 5))

if __name__ == "__main__":
    main()
