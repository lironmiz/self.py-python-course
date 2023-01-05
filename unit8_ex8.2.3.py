# exercise 8.2.3 from unit 8
'''
Write a function called mult_tuple defined as follows:

def mult_tuple(tuple1, tuple2):
The function accepts as parameters two members of the tuple type.
The function returns a tuple containing all the pairs that can be created from the members of the tuples passed as arguments.

Running examples of the mult_tuple function
>>> first_tuple = (1, 2)
>>> second_tuple = (4, 5)
>>> mult_tuple(first_tuple, second_tuple)
((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))
>>> first_tuple = (1, 2, 3)
>>> second_tuple = (4, 5, 6)
>>> mult_tuple(first_tuple, second_tuple)
((1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), ( 3, 6), (4, 1), (5, 1), (6, 1), (4, 2), (5, 2), (6, 2), (4, 3), (5, 3), (6, 3))
'''

def mult_tuple(tuple1, tuple2):
    def combinations(t1, t2):
        # create a list of tuples with all combinations of elements from t1 and t2
        comb = [(x, y) for x in t1 for y in t2]
        # add all combinations of elements from t2 and t1
        comb += [(y, x) for x in t1 for y in t2]
        return comb
    
    return combinations(tuple1, tuple2)

