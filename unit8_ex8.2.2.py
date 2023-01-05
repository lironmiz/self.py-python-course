# exercise 8.2.2 from unit 8
'''
Exercise 8.2.2
Write a function called sort_prices defined as follows:

def sort_prices(list_of_tuples):
The function receives a list of tuples that each have an item and a price.
The function returns a list of tuples sorted by the price of the items in them from the largest to the smallest.

Define the list of tuples that the function receives according to the following form:

[('item', 'price'), ('item', 'price'), ('item', 'price')]
Note that all members are of string type and price is written as a non-integer number.

Running examples of the sort_prices function
>>> products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
>>> sort_prices(products)
[('bread', '9.0'), ('milk', '5.5'), ('candy', '2.5')]
'''

def sort_prices(list_of_tuples):
    def get_price(tuple):
        return float(tuple[1])
    
    # sort the list of tuples by the price of the item in each tuple
    sorted_list = sorted(list_of_tuples, key=get_price, reverse=True)
    return sorted_list

# test the function
products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(products))
