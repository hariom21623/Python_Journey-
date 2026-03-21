while True:
    print("\n--- Simple Calculator ---")
    
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %, **, //): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed")
    elif operator == "%":
        print("Result:", num1 % num2)
    elif operator == "**":
        print("Result:", num1 ** num2)
    elif operator == "//":
        if num2 != 0:
            print("Result:", num1 // num2)
        else:
            print("Error: Division by zero is not allowed")
    else:
        print("Invalid operator")

    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for using calculator.")
        break