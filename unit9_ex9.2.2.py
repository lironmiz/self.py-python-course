# exersice 9.2.2 from unit 9
'''
Write a function called copy_file_content defined as follows:

def copy_file_content(source, destination):
The function accepts as parameters two strings representing file paths.
The function copies the contents of the source file to the destination file.

An example of an input file and the execution of the copy_file_content function:
A file called copy.txt:

Copy this text to another file.
A file called paste.txt:

-- some random text --
Running the function copy_file_content with the files copy.txt and paste.txt:

>>> copy_file_content("copy.txt", "paste.txt")
The paste.txt file after the above run of the copy_file_content function:

Copy this text to another file.
'''

def copy_file_content(source, destination):
    with open(source, 'r') as src_file:
        with open(destination, 'w') as dest_file:
            dest_file.write(src_file.read())

def main():
    copy_file_content("copy.txt", "paste.txt")

if __name__ == "__main__":
    main()
    
