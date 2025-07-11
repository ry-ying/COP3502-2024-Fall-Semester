num1 = float(input("Enter first operand: ")) #Float inputs to take in the first and second operand. Could be decimal or negative so int() does not work.
num2 = float(input("Enter second operand: "))

print("\nCalculator Menu\n---------------\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

operation = int(input("Which operation do you want to perform? ")) # Int to take in the calculator operation, since it is whole numbers

if operation == 1: #Selection depending on the user's operation.
    print(f"The result of the operation is {num1+num2}. Goodbye!") # f-string to handle the output.3
    
elif operation == 2:
    print(f"The result of the operation is {num1-num2}. Goodbye!")
elif operation == 3:
    print(f"The result of the operation is {num1*num2}. Goodbye!")
elif operation == 4:
    print(f"The result of the operation is {num1/num2}. Goodbye!")
else:
    print("Error: Invalid selection! Terminating program.")