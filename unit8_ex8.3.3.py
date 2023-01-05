# exercise 8.3.3 from unit 8
'''
Write a function called count_chars defined like this:

def count_chars(my_str):
The function accepts a string as a parameter.
The function returns a dictionary, so that each element in it is a pair consisting of a key: a character from the passed string (not including spaces), and an array: the number of times the character appears in the string.

An example of running the count_chars function:
>>> magic_str = "abra cadabra"
>>> count_chars(magic_str)
{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
'''

def main():
    def count_chars_helper(my_str):
        char_counts = {}
        for char in my_str:
            if char == ' ':
                continue
            if char not in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] += 1
        return char_counts

    magic_str = "abra cadabra"
    print(count_chars_helper(magic_str))

main()

