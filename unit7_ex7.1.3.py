# exercise 7.1.3 from unit 7
'''
Here are two pieces of code that include a while loop. Match each loop with the output obtained when it runs.

Choose the output obtained by running each of the loops.

Guidelines

It is recommended to use tracking tables.
'''

# 1

i = 11
while i > 0:
  i -=1
  if i == 5:
    break
   print(i)
  
# Answer: 10 next line 9 than 8 7 6

# 2

i = 11
while i > 0:
  i -=1
  if i == 5:
    continue
   print(i)

# Answer: 10 next line 9 than 8 7 6 4 3 2 1 0
