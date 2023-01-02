'''
The legend "The Three Little Pigs" tells about three pigs who lived under the threat of a wolf. In order to provide themselves with shelter from him, they began to gather together building materials.
Write a program that will display the total number of bricks collected by the pigs, and the number of bricks available to each pig, according to the following instructions.

Guidelines
The program will receive as input a three-digit number (assume that the input is correct). Each digit in this number represents the number of bricks collected by another pig.
The program will print the following output:
The total number of bricks collected by the piggies (ie the sum of the three digits)
The number of bricks that each pig will get if they divide the total number of bricks is equal among all
The remainder of the distribution of bricks (as distributed in the previous section)
True if the sum is divided between the three pigs without a remainder, and False otherwise. Note, do not use a conditional statement
Do not use loops.
'''
#ex 2.3.3

blocks_num = int(input('\n Enter three digits number: '))
num1 = int(blocks_num / 100)
num2 = int((blocks_num / 10) % 10)
num3 = blocks_num % 10
sum_blocks = num1 + num2 + num3
print('\n', num1, num2, num3)
print('\n', sum_blocks)
print('\n', int(sum_blocks / 3))
print('\n', sum_blocks  % 3 == 0)
