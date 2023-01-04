# exercise 6.3.2 from unit 6
'''
Write a function named longest defined as follows:

def longest(my_list):
The function accepts a list consisting of strings and returns the longest string.

An example of using the longest function
>>> list1 = ["111", "234", "2000", "goru", "birthday", "09"]
>>> longest(list1)
birthday

Guidelines
Do not use loops.
'''

def longest(my_list):
    return max(my_list, key=len)

def main():
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    longest_string = longest(list1)
    print(longest_string)

if __name__ == "__main__":
    main()
