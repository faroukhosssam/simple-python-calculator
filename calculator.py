num1 = float(input("Enter first number: "))
choose = input("Choose operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if choose == "+":
    print("Result:", num1 + num2)
elif choose == "-":
    print("Result:", num1 - num2)
elif choose == "*":
    print("Result:", num1 * num2)
elif choose == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation, please choose (+, -, *, /)")
