# exercise 5.3.6 from unit 5

'''
Write a function called filter_teens defined as follows:

def filter_teens(a, b, c):
The function receives three values representing ages: a, b, c and returns their sum.

Guidelines
If the function is called with no parameters, the default value of each age is 13.
If one of the values represents the age of teenagers between 13 and 19 (including them)
but excluding the ages 15 and 16 - adjust its value using the function described below,
so that it is calculated as 0.

Write a helper function fix_age defined as follows:
def fix_age(age):
The function receives a number that represents an age and returns it corrected 
according to the rules above. Call the fix_age function from within the filter_teens
function so that you don't repeat the age correction code three times.

Running examples of the filter_teens function

>>> filter_teens()
0
>>> filter_teens(1, 2, 3)
6
>>> filter_teens(2, 13, 1)
3
>>> filter_teens(2, 1, 15)
18
'''
def fix_age(age):
    if age >= 13 and age <= 19 and age not in (15, 16):
        return 0
    return age


def filter_teens(a=13, b=13, c=13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    return a + b + c

print(filter_teens())  # 0
print(filter_teens(1, 2, 3))  # 6
print(filter_teens(2, 1, 15))  # 18
  
  
