# exercise 5.3.5 from unit 5

'''
Write a function called distance defined as follows:

def distance(num1, num2, num3):
The function accepts three integers: num1, num2, num3.

The function returns true if both conditions are met:

One of the numbers num2 or num3 is "close" to num1. "Near" = absolute distance 1.
One of the numbers num2 or num3 is "far" from the other two numbers. "Far" = absolute distance 2 or more.
Running examples of the distance function
>>> distance(1, 2, 10)
True
>>> distance(4, 5, 3)
False
Guidelines
You can use the built-in function (abs(num) which calculates the absolute value of a number.

'''
def distance(num1, num2, num3):
    # Check if one of the numbers is "close" to num1
    cond1 = abs(num1 - num2) == 1 or abs(num1 - num3) == 1
    # Check if one of the numbers is "far" from the other two
    cond2 = abs(num2 - num3) >= 2 and abs(num2 - num1) >= 2 or abs(num3 - num1) >= 2
    # Return True if both conditions are met, False otherwise
    return cond1 and cond2

print(distance(1, 2, 10)) # True

print(distance(4, 5, 3)) # False


  
