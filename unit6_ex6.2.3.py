# exersice 6.2.3 from unit 6
'''
Write a function called format_list defined as follows:

def format_list(my_list):
The function receives a list of strings of even length. The function returns a string containing the members of the list in the even positions, separated by a comma and a space, and also the last member with the inscription and before it.

An example of running the format_list function
>>> my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
>>> format_list(my_list)
hydrogen, lithium, boron, and magnesium

Guidelines
Do not use loops.
'''
def format_list(my_list):
    formatted_list = ', '.join(my_list[::2])
    return f"{formatted_list} and {my_list[-1]}"


def main():
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    formatted_list = format_list(my_list)
    print(formatted_list)

if __name__ == "__main__":
    main()
  
