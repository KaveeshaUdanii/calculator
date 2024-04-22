# List to store the previous operations
calculation_history = []

# Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    if b == 0:
        print("float division by zero")
        return None
    return a / b

# Function to perform exponentiation
def power(a, b):
    return a ** b

# Function to calculate remainder
def remainder(a, b):
    if b == 0:
        print("Error: Modulo by zero")
        return None
    return a % b

# Function to handle arithmetic operations
def select_op(choice):
    if choice in ('+', '-', '*', '/', '^', '%'):
        num1 = input("Enter first number: ")
        print(num1)
        if num1.replace('.', '').isdigit():
            num2 = input("Enter second number: ")
            print(num2)
            if num2.replace('.', '').isdigit():
                num1 = float(num1)
                num2 = float(num2)
                if choice == '+':
                    result = add(num1, num2)
                elif choice == '-':
                    result = subtract(num1, num2)
                elif choice == '*':
                    result = multiply(num1, num2)
                elif choice == '/':
                    result = divide(num1, num2)
                elif choice == '^':
                    result = power(num1, num2)
                elif choice == '%':
                    result = remainder(num1, num2)
                else:
                    print("Something went wrong")
                
                if result is not 0:
                    operation = f"{num1} {choice} {num2} = {result}"
                    calculation_history.append(operation)
                    print(operation)
            else:
                print("Not a valid number, please enter again")
        else:
            print("Not a valid number, please enter again")
    elif choice == '#':
        return -1
    elif choice == '$':
        print("Resetting...")
        calculation_history.clear()
        return 0
    elif choice == '?':
        history()
    else:
        print("Unrecognized operation")

# Function to display calculation history
def history():
    if calculation_history:
        #print("Calculation History:")
        for index, operation in enumerate(calculation_history, start=1):
            print(f"{operation}")
    else:
        print("No past calculations to show")

# Main loop
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")

    # Take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    if select_op(choice) == -1:
        # Program ends here
        print("Done. Terminating")
        exit()
