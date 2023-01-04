# exercise 7.2.4 from unit 7
'''
Write a function called seven_boom which simulates the game "Seven Boom". The function is defined as:

def seven_boom(end_number):
The function accepts an integer, end_number.
The function returns a list in the range of numbers 0 to end_number inclusive, with certain numbers replaced by the string 'BOOM', if they meet one of the following conditions:

The number is a multiple of the number 7.
The number contains the digit 7.
Example of running the seven_boom function:
>>> print(seven_boom(17))
['BOOM', 1, 2, 3, 4, 5, 6, 'BOOM', 8, 9, 10, 11, 12, 13, 'BOOM', 15, 16, 'BOOM']
'''

def seven_boom(end_number):
    result = []
    for i in range(1, end_number+1):
        if i % 7 == 0 or '7' in str(i):
            result.append('BOOM')
        else:
            result.append(i)
    return result

def main():
    print(seven_boom(21))

if __name__ == '__main__':
    main()
