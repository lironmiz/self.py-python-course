# exercise 8.2.1 from unit 8 
'''
Given the plan:

data = ("self", "py", 1.543)
format_string = "Hello"

print(format_string % data)
We updated the format_string variable to print:

Hello self.py learner, you have only 1.5 units left before you master the course!
Guidelines
Use the data variable.
Note that only one digit is printed after the period (ie the number 1.5).
'''

def main():
    data = ("self", "py", 1.543)
    data = ("self", "py", "1.543")
    format_string = "Hello %s learner, you have only %.1f units left before you master the course!"
    print(format_string % (data[0], float(data[2])))

if __name__ == "__main__":
    main()
