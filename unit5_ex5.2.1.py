# exercise 5.2.1 from unit 5
'''
Here are four code snippets for practicing the topic "local and global variables". Repeat the topic again if necessary and answer:
What will be printed when we run each of the code snippets
Choose the expected output for each piece of code. Try to answer without using an interpreter.
'''

# 1: 

a = 1

def foo1():
  print(a)
  
foo1()
print(a)

# Answer: output 1 and 1

# 2:

b = 1

def foo2():
  b=2
  print(b)
  
foo2()
print(b)

# Answer: 2 and after 1

# 3:

c = 1

def foo3():
  c = c + 1
  print(c)
  
foo3()
print(c)

# Answer: error 

# 4:

d = 1

def foo4():
  global d
  d = 2
  print(d)
  
foo4()
print(d)

# Answer: 2 and 2

