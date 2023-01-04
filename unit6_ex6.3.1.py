# exercise 6.3.1 from unit 6 
'''
Write a function called are_lists_equal defined as follows:

def are_lists_equal(list1, list2):
The function accepts two lists containing members of the int and float types only. The function returns true if the two lists contain exactly the same elements (even if in different order), otherwise, the function returns false.

An example of using the are_lists_equal function
>>> list1 = [0.6, 1, 2, 3]
>>> list2 = [3, 2, 0.6, 1]
>>> list3 = [9, 0, 5, 10.5]
>>> are_lists_equal(list1, list2)
True
>>> are_lists_equal(list1, list3)
False

Guidelines
Do not use loops.
'''

def are_lists_equal(list1, list2):
    return set(list1) == set(list2)

def main():
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]
    print(are_lists_equal(list1, list2))
    print(are_lists_equal(list1, list3))

if __name__ == "__main__":
    main()
