def perform_operation (num1, num2, operation):
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = str(input("Enter the operation (add, subtract, multiply, divide): ")).strip().lower()
    match operation:
     case "add":
        print(f"The result is {num1 + num2}.")
     case "subtract":
        print(f"The result is {num1 - num2}.")
     case "multiply":
        print(f"The result is {num1 * num2}.")
     case "divide":
        if num2 == 0:
            print("Cannot divide by zero.")
        else :
            print(f"The result is {num1 / num2}.")
    result = perform_operation (num1, num2, operation)
    print(f"Result: {result}")
   #  if operation == 'add':
   #      return num1 + num2
   #  elif operation == 'subtract':
   #      return num1 - num2
   #  elif operation == 'multiply':
   #      return num1 * num2
   #  elif operation == 'divide':
   #      if num2 == 0:
   #          return "Error: Division by zero is not allowed."
   #      return num1 / num2
   #  else:
   #      return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."
