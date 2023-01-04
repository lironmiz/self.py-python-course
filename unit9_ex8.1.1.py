# exersice 8.1.1 from unit 8
'''
Here are four pieces of code. Choose the output obtained by running each of the code segments.
'''

# 1:
tuple_one = (1, 2, 3, 4 )
tuple_one[1:-1]

# Answer: (2,3)

# 2:
tuple_two = (2, 5, 8, 3, 6, 9)
for i in range(0, len(tuple_two), 3):
  print(tuple_two[i])

# Answer: 2 and after 3

# 3:
tuple_three = (2, 1, 3)
tuple_three.sort()

# Answer: error

# 4:
tuple_four = (4, 2, 3)
sorted(tuple_four)

# Answer: [2, 3, 4]
