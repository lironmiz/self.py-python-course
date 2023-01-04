# exercise 7.2.6 from unit 7
'''
Write a program that receives from the user a single string representing a list of products 
for shopping, separated by commas without spaces.
An example of an input string: "Milk,Cottage,Tomatoes".

The program asks the user to key in a number (digit) in the range of one to nine
(there is no need to check the correctness of the input).
Depending on the number received, perform one of the following actions, according to
the following breakdown:

The program asks the user to key in a number (digit) in the range of one to nine
(there is no need to check the correctness of the input).
Depending on the number received, perform one of the following actions, according
to the following breakdown:

1.Printing the list of products
2.Printing the number of products in the list
3.Printing the answer to the test "Is the product on the list?" (The user will be asked to enter a product name)
4.Printing the answer to the test "How many times does a certain product appear?" (The user will be asked to enter a product name)
5.Deleting a product from the list (the user will be asked to tap a product name, only one product will be deleted)
6.Adding a product to the list (the user will be asked to tap a product name)
7.Printing all invalid products (a product is invalid if its length is less than 3 or it contains characters other than letters)
8.Removing all existing duplicates in the list

Output

Please note, after the user makes a selection, the user will return to the main menu until he
selects the exit (he will press the number 9).

Guidelines
Transfer the products that the program accepts to the list.
Use additional functions of your choice.

'''

def main():
    products = input("Enter a string of products separated by commas: ").split(",")

    while True:
        print("Menu:")
        print("1. Print the list of products")
        print("2. Print the number of products in the list")
        print("3. Check if a product is on the list")
        print("4. Count the number of occurrences of a product")
        print("5. Delete a product from the list")
        print("6. Add a product to the list")
        print("7. Print invalid products")
        print("8. Remove duplicates from the list")
        print("9. Exit")

        choice = int(input("Enter your choice 1-9: "))
        if choice == 1:
            print(products)
        elif choice == 2:
            print(len(products))
        elif choice == 3:
            product = input("Enter a product name: ")
            if product in products:
                print("The product is on the list.")
            else:
                print("The product is not on the list.")
        elif choice == 4:
            product = input("Enter a product name: ")
            print(products.count(product))
        elif choice == 5:
            product = input("Enter a product name: ")
            products.remove(product)
        elif choice == 6:
            product = input("Enter a product name: ")
            products.append(product)
        elif choice == 7:
            invalid_products = [p for p in products if len(p) < 3 or not p.isalpha()]
            print(invalid_products)
        elif choice == 8:
            products = list(set(products))
        elif choice == 9:
            break

if __name__ == "__main__":
    main()
