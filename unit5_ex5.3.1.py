# exercise 5.3.1 from unit 5
# in fron of you there is the method remainder 

def remainder(base, divide_by=2, show_greeting=True):
    if show_greeting:
        print("Welcome to my function")
    print(base % divide_by)
    
# tell which of the calss will print the following output:
# Welcome to my function
# 1
# Answer:
remainder(9, 8, True)

remainder(9)
