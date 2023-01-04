# exercise 7.1.4 from unit 7
'''
Write a function called squared_numbers defined as follows:

def squared_numbers(start, stop):
The function accepts two integers, start and stop (assume that: start <= stop). The function returns a list containing all the squares of the numbers between start and stop (inclusive).

Guidelines

Use a while loop only.

Running examples of the squared_numbers function
>>> squared_numbers(4, 8)
[16, 25, 36, 49, 64]
>>> squared_numbers(-3, 3)
[9, 4, 1, 0, 1, 4, 9]

'''

def squared_numbers(start, stop):
    result = []
    i = start
    while i <= stop:
        result.append(i ** 2)
        i += 1
    return result

def main():
    print(squared_numbers(4, 8))  # print [16, 25, 36, 49, 64]
    print(squared_numbers(-3, 3))  # print [9, 4, 1, 0, 1, 4, 9]
    print(squared_numbers(-2, 2))  # print [4, 1, 0, 1, 4]
    print(squared_numbers(0, 5))  # print [0, 1, 4, 9, 16]
    print(squared_numbers(2, 2))  # print [4]

if __name__ == "__main__":
    main()
