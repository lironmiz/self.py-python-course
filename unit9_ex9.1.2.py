# exercise 9.1.2 from unit 9
'''
Write a program that receives from the user:

Path to text file (string)
Name of one of the operations: rev, sort or last (string)
The file we return is passed as an argument containing lines of lowercase word sequences separated by a single space.

According to the name of the action received from the user, the program performs:

sort - the program prints all the words in the transferred file as a sorted list in alphabetical order, without duplicates.
rev - the program prints the characters in each line in the file in reverse order, i.e. from the end to the beginning.
last - the program receives another parameter from the user which is an integer (n), and prints the last n lines in the file (assume that the number is positive and less than or equal to the number of lines in the file).
An example of an input file and lectures of the program
A file called sampleFile.txt:

i believe i can fly i believe i can touch the sky
I think about it every night and day spread my wings and fly away
Run the program on the file sampleFile.txt:

>>> Enter a file path: c:\sampleFile.txt
>>> Enter a task: sort
['about', 'and', 'away', 'believe', 'can', 'day', 'every', 'fly', 'i', 'it', 'my', 'night', ' sky', 'spread', 'the', 'think', 'touch', 'wings']
>>> Enter a file path: c:\sampleFile.txt
>>> Enter a task: rev
yks eht hcuot nac i eveileb i ylf nac i eveileb i
yawa ylf dna sgniw ym daerps yad dna thgin yreve ti tuoba kniht i
>>> Enter a file path: c:\sampleFile.txt
>>> Enter a task: last
>>> Enter a number: 1
I think about it every night and day spread my wings and fly away
'''

def main():
    file_path = input("Enter a file path: ")
    task = input("Enter a task: ")
    with open(file_path, 'r') as f:
        lines = f.readlines()
    if task == 'sort':
        words = sorted(set(line.split() for line in lines))
        print(words)
    elif task == 'rev':
        reversed_lines = [line[::-1] for line in lines]
        print(reversed_lines)
    elif task == 'last':
        n = int(input("Enter a number: "))
        print(lines[-n:])

main()
