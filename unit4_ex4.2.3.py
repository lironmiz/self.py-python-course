# exercise 4.2.3 from unit 4
'''
Write a program that converts a temperature in degrees Celsius to a
temperature in degrees Fahrenheit.
The program receives a temperature from the user: either
in degrees Celsius, with the suffix C, or in degrees Fahrenheit, with the suffix F.
If the temperature is in degrees Celsius, convert it to degree
s Fahrenheit, and if the temperature is in degrees Fahrenheit, convert it to degrees Celsius.
  
Guidelines
The temperature can be either an integer or a non-integer (int or float).
The suffix can be a lowercase letter or an uppercase letter (c, C, f, F).
'''

temp = input("Enter a temperature: ")

# Check if temperature is in Celsius or Fahrenheit
if temp[-1] == 'C':
  # Convert Celsius to Fahrenheit
  temp = float(temp[:-1]) * 9.0 / 5.0 + 32.0
  print(f"{temp}F")
else:
  # Convert Fahrenheit to Celsius
  temp = (float(temp[:-1]) - 32.0) * 5.0 / 9.0
  print(f"{temp}C")
