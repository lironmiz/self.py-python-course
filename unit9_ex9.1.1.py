# exercise 9.1.1 from unit 9
'''
Write a function called are_files_equal defined as follows:

def are_files_equal(file1, file2):
The function accepts as parameters paths of two text files (strings).

The function returns true (True) if the files are identical in content, otherwise returns false (False).

An example of running the are_files_equal function with different files
>>> are_files_equal("c:\vacation.txt", "c:\work.txt")
False
'''

def are_files_equal(file1, file2):
    # open the first file and read its contents
    with open(file1, 'r') as f:
        contents1 = f.read()
    # open the second file and read its contents
    with open(file2, 'r') as f:
        contents2 = f.read()
    # compare the contents of the two files
    return contents1 == contents2

# test the function
print(are_files_equal("c:\\vacation.txt", "c:\\work.txt"))
