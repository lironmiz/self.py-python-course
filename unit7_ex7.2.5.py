# exercise 7.2.5 from unit 7
'''
Write a function called sequence_del defined as follows:

def sequence_del(my_str):
The function accepts a string and deletes the letters appearing in sequence. That is, the function returns a string in which only one character appears from each sequence of identical characters in the input string.

Running examples of the sequence_del function
>>> sequence_del("ppyyyyythhhhhooonnnnn")
python
>>> sequence_del("SSSSsssshhhh")
'ssh'
>>> sequence_del("Heeyyy yyouuuu!!!")
'Hey you!'
'''

def sequence_del(my_str):
    result = ""
    prev_char = ""
    for char in my_str:
        if char != prev_char:
            result += char
        prev_char = char
    return result

def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    print(sequence_del("SSSSsssshhhh"))
    print(sequence_del("Heeyyy yyouuuu!!!")) 

if __name__ == "__main__":
    main()
