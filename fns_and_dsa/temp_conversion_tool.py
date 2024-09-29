global FAHRENHEIT_TO_CELSIUS_FACTOR
global CELSIUS_TO_FAHRENHEIT_FACTOR
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temp_input = float(input("Enter the temperature to convert:"))
unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit_input == 'C':
    converted_temp = convert_to_fahrenheit(temp_input)
    print(f"{temp_input}°C is equal to {converted_temp:.2f}°F")
elif unit_input == 'F':
    converted_temp = convert_to_celsius(temp_input)
    print(f"{temp_input}°F is equal to {converted_temp:.2f}°C")
else:
    print("Invalid temperature. Please enter a numeric value")
