# exercise 5.1.1 from unit 5
'''
Here is a code snippet for defining the mystery function and after the definition,
two code snippets to run:
'''
# section 1
def mystery(index):
     print("z" * len(index))
# section 2 
mystery(3)
# section 3
func = mystery
func("python")

# Mark all the correct sentences regarding the mystery function and the run sections that follow it.

# Answer:
# A: the var index is a paramter to the function mystery
# D: the value 3 is argument that been pass to the function func 
# E: mystery and func is pointing to the same location on memory 
# G: the output from line 12 is zzzzzz
# H: The mystery function is called in code section number 2
