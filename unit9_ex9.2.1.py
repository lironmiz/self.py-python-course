# exercise 9.2.1 from unit 9
'''
we have empty file called empty.txt 
and we need to tell what will be print

'''

with open("empty.txt", "w") as input_file:
    input_file.write("So, call me mabye?")
    print(input_file.read())
    
# Answer: error io.UnsupportedOperation
