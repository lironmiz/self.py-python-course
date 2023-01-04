# exercise 7.2.1 from unit 7
'''
Write a function called is_greater defined as follows:

def is_greater(my_list, n):
The function accepts two parameters: a list and a number n.
The function returns a new list containing all the elements that are greater than the number n.

An example of running the is_greater function:
>>> result = is_greater([1, 30, 25, 60, 27, 28], 28)
>>> print(result)
[30, 60]
'''

def is_greater(my_list, n):
    result = []
    for element in my_list:
        if element > n:
            result.append(element)
    return result

def main():
    result = is_greater([1, 30, 25, 60, 27, 28], 28)
    print(result)  # print [30, 60]
    result = is_greater([1, 2, 3, 4, 5, 6], 3)
    print(result)  # print [4, 5, 6]
    result = is_greater([10, 20, 30, 40], 15)
    print(result)  # print [20, 30, 40]
    result = is_greater([1, 2, 3, 4, 5, 6], 6)
    print(result)  # print []

if __name__ == "__main__":
    main()
