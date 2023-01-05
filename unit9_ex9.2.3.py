# exercise 9.2.3 from unit 9
'''
Write a function called who_is_missing defined as follows:

def who_is_missing(file_name):
The function accepts as a parameter a path to a text file (string).
The file we return is passed as an argument and contains a list of integers from 1 to some n, which are not sorted, separated by commas, when one of the numbers in the sequence disappears (that is, missing from the sorted list).

The operation of the who_is_missing function:
A. The function returns the missing number in the sequence (int).
B. The function writes the missing number in sequence to a new file called found.txt.

An example of an input file and the execution of the who_is_missing function
A file called findMe.txt:

8,1,9,7,4,6,3,2
Running the who_is_missing function on the findMe.txt file:

>>> who_is_missing("c:\findMe.txt")
5
After the above run of the who_is_missing function, a new file called found.txt is created:

5
'''

def who_is_missing(file_name):
    # Read the file and extract the numbers
    with open(file_name, 'r') as f:
        numbers = [int(num) for num in f.read().split(',')]

    # Find the missing number
    expected_sum = sum(range(1, len(numbers) + 1))
    actual_sum = sum(numbers)
    missing_number = expected_sum - actual_sum

    # Write the missing number to a new file
    with open('found.txt', 'w') as f:
        f.write(str(missing_number))

    return missing_number

def main():
    result = who_is_missing("c:\findMe.txt")
    print(result)

if __name__ == "__main__":
    main()
