# exercise 5.3.3 from unit 5
 
# Here is a function called show_date
def show_date(day, month, year=17):
    print(day, "/", month, "/", year)
    
# Choose the output that is obtained for each of the following calls to the function

# 1

show_date(day=15, month=12, year=17)

# output: 15/12/17

# 2

show_date(month=15, day=12)

# output: 12/15/17

# 3

show_date(17, 12)

# output: 17/12/17

# 4

show_date(15, year=12)

# output: TypeError
