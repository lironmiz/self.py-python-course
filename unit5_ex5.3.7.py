# exercise 5.3.7 from unit 5
'''
We would like to connect chocolate cubes to a row that is x cm long. We have small
chocolate cubes 1 cm long and large chocolate cubes 5 cm long.

For the purpose of the task, write a function called chocolate_maker defined as follows:

def chocolate_maker(small, big, x):
The function receives the number of small cubes (small), the number of large cubes (big)
and the desired line length (x). The function returns true if it is possible to create
a line of length x using the number of chocolate cubes it received, all or some.

Guidelines
Do not use loops.

Running examples of the chocolate_maker function
>>> chocolate_maker(3, 1, 8)
True
>>> chocolate_maker(3, 1, 9)
False
>>> chocolate_maker(3, 2, 10)
True
'''

def chocolate_maker(small, big, x):
    one_total = small * 1
    five_total = big * 5
    if one_total + five_total == x or five_total == x or one_total == x:
        return True
    elif x - one_total > 0:
        if (x - one_total) % 5 == 0:
            return x <= five_total
        else:
            return False
    else:
        return True
