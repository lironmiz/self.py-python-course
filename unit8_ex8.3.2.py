# exercies 8.3.2 from unit 8
'''
Create a dictionary with a name of your choice and initialize it according to the 
following table:

Mariah first_name
Carey last_name
27.03.1970 (string) birth_date
Sing, Compose, Act (list) hobbies

Write a program that performs the following actions, depending on the digit that the user
pressed:

Print Maria's last name to the screen.
Print to the screen the month in which Maria was born.
Print to the screen the number of hobbies Maria has.
Print to the screen the last hobby in Maria's list of hobbies.
Add the hobby "Cooking" to the end of the list of hobbies.
Turn the date of birth type into a tuple that includes 3 numbers
(day, month and year - from left to right) and print it.
Add a new key called age which includes Maria's age and present it.
Guidelines
Ask the user to enter an input (a number between 1 and 7) and assume that the input
is correct.
'''

def main():
    # create a dictionary with Maria's information
    mariah = {
        'first_name': 'Mariah',
        'last_name': 'Carey',
        'birth_date': '27.03.1970',
        'hobbies': ['Sing', 'Compose', 'Act']
    }

    user_input = int(input("Enter a number between 1 and 7: "))

    def perform_action(mariah, user_input):
        if user_input == 1:
            print(mariah['last_name'])
        elif user_input == 2:
            month = mariah['birth_date'].split('.')[1]
            print(month)
        elif user_input == 3:
            print(len(mariah['hobbies']))
        elif user_input == 4:
            print(mariah['hobbies'][-1])
        elif user_input == 5:
            mariah['hobbies'].append('Cooking')
            print(mariah['hobbies'])
        elif user_input == 6:
            birth_date = tuple(mariah['birth_date'].split('.'))
            print(birth_date)
        elif user_input == 7:
            mariah['age'] = 2023 - int(mariah['birth_date'].split('.')[2])
            print(mariah['age'])

    perform_action(mariah, user_input)

# call the main function
main()
