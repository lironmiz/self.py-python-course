# exercies 8.3.4 from unit 8
'''
We are nearing the end of the course and at this stage you can combine the topics
learned throughout the course, explore additional options yourself and apply everything
in writing the code.

In this exercise, write a function called inverse_dict defined as follows:

def inverse_dict(my_dict):
The function accepts as a parameter a dictionary.
The function returns a new dictionary with a "reverse" mapping: each key in the passed
dictionary is a value in the returned dictionary and each value in the passed dictionary 
is a key in the returned dictionary.

Guidelines

The inversion between keys and values may create keys that appear more than once. Therefore,
display the values in the returned dictionary as a list, which may contain one or more values
The returned lists should be sorted (it can be assumed that the values in the dictionary
are of the same type).

'''

def main():
    def inverse_dict_helper(my_dict):
        inverted_dict = {}
        for key, value in my_dict.items():
            if value not in inverted_dict:
                inverted_dict[value] = [key]
            else:
                inverted_dict[value].append(key)
        for value in inverted_dict.values():
            value.sort()
        return inverted_dict

    my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 2}
    print(inverse_dict_helper(my_dict))

main()

