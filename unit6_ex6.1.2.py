# exercise 6.1.2 from unit 6
'''
Write a function called shift_left. The function accepts a list of length 3 and returns a new list shifted one step to the left.

function definition
def shift_left(my_list):
Examples of running the shift_left function
>>> shift_left([0, 1, 2])
[1, 2, 0]
>>> shift_left(['monkey', 2.0, 1])
[2.0, 1, 'monkey']
'''

def shift_left(my_list):
    return my_list[1:] + [my_list[0]]
  
def main():
    print(shift_left([0, 1, 2])) # [1, 2, 0]
    print(shift_left(['monkey', 2.0, 1])) # [2.0, 1, 'monkey']

if __name__ == "__main__":
    main()
