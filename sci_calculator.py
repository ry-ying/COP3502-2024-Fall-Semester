import math # Importing the math module.

# Have boolean to loop, and int value to store how many calculations performed.
calculatorActive = True
calculationsPerformed = 0

# Total to use to calculate stats, old results to store RESULT (extra credit)
currentTotal = 0
oldResult = 0

# Function to handle operands, just makes the code neater.
def return_operands():
    operand1 = input("Enter first operand: ")
    operand2 = input("Enter second operand: ")

    if operand1 == "RESULT":
        operand1 = oldResult
    if operand2 == "RESULT":
        operand2 = oldResult

    return float(operand1), float(operand2)

# Main loop
while calculatorActive:

# Prints current result and calculator menu
    print(f"Current Result: {float(oldResult)}\n\n")
    print("Calculator Menu\n---------------\n0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average")

# Menu loop to keep looping the menuSelect input until receiving a valid operation
    while True:
        menuSelect = int(input("Enter Menu Selection: "))
        if menuSelect == 0:
            calculatorActive = False
            print("\n\nThanks for using this calculator. Goodbye!")
            break
        elif menuSelect == 1: #Each operation uses return_operands() function to receive operands and then breaks out of the menuSelect loop.
            num1, num2 = return_operands()
            sol = num1 + num2
            currentTotal += sol
            oldResult = sol
            calculationsPerformed += 1
            break
        elif menuSelect == 2:
            num1, num2 = return_operands()
            sol = num1 - num2
            currentTotal += sol
            oldResult = sol
            calculationsPerformed += 1
            break
        elif menuSelect == 3:
            num1, num2 = return_operands()
            sol = num1 * num2
            currentTotal += sol
            oldResult = sol
            calculationsPerformed += 1
            break
        elif menuSelect == 4:
            num1, num2 = return_operands()
            sol = num1/num2
            currentTotal += sol
            oldResult = sol
            calculationsPerformed += 1
            break
        elif menuSelect == 5:
            num1, num2 = return_operands()
            sol = math.pow(num1, num2)
            currentTotal += sol
            oldResult = sol
            calculationsPerformed += 1
            break
        elif menuSelect == 6:
            num1, num2 = return_operands()
            sol = math.log(num2, num1)
            currentTotal += sol
            oldResult = sol
            calculationsPerformed += 1
            break
        elif menuSelect == 7: #Statistics, basic math to calculate the statistics (using floats, of course.)
            if calculationsPerformed > 0:
                print(f"Sum of calculations: {currentTotal}")
                print(f"Number of calculations: {calculationsPerformed}")
                print(f"Average of calculations: {round(currentTotal/calculationsPerformed,2)}")
            else:
                print("Error: No calculations yet to average!")

        else:
            print("Error: Invalid selection!")