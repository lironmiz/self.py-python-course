# exercise 4.2.4 from unit 4

'''
Write a program that accepts a date from the user in the format dd/mm/yyyy
and prints the day of the week for the entered date.

examples:
>>> Enter a date: 01/01/2000
Saturday
>>> Enter a date: 27/11/2051
Monday

Directions: Look for documentation about the calendar library and the weekday function.

'''

import calendar

date_str = input("Enter a date (dd/mm/yyyy): ")

# Split date string into day, month, and year
day, month, year = map(int, date_str.split('/'))

# Get the day of the week using the weekday() method
day_of_week = calendar.weekday(year, month, day)

# Convert day of the week to a string
day_of_week_str = calendar.day_name[day_of_week]

print(day_of_week_str)
