# exercise 6.2.4 from unit 6

'''
Write a function called extend_list_x defined as follows:
def extend_list_x(list_x, list_y):
The function receives two lists list_y, list_x. The function expands list_x (changes it) so that it also contains list_y at the beginning, and returns list_x.

An example of running the extend_list_x function
>>> x = [4, 5, 6]
>>> y = [1, 2, 3]
>>> extend_list_x(x, y)
[1, 2, 3, 4, 5, 6]
Guidelines
Do not use the '+' operator.
Do not use the extend method.

Attention, this is a challenge exercise... ready? Take your time, try to think outside
the box and look for the trick to solve it.
'''

def extend_list_x(list_x, list_y):
    list_x[:0] = list_y
    return list_x

def main():
    x = [4, 5, 6]
    y = [1, 2, 3]
    extended_list = extend_list_x(x, y)
    print(extended_list)

if __name__ == "__main__":
    main()
