# exercise 8.3.1 from unit 8
'''
given the dict:
my_dict = {(1, 2): 1, (2, 3): 2}

Here are four pieces of code. Choose the output obtained by running each of the code segments.

'''
# 1:

my_dict = {(1, 2): 1, (2, 3): 2}

for key in my_dict.keys():
  print(key)
  
# Answer: (1,2) and (2,3)

# 2:

for value in my_dict.values():
  print(value)
  
# Answer: 1 and 2

# 3:

print(len(my_dict))
  
# Answer: 2

# 4:

print(my_dict[1])
  
# Answer: KeyError

# 5:

print(my_dict[1, 2])
  
# Answer: 1

