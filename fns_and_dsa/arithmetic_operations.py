def perform_operation():
    print("Arithmetic Operations")
    global num1, num2, operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
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
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")