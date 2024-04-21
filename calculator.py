#TODO: Write the functions for arithmetic operations here
#These functions should cover Task 2
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
        return 0
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

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function should cover Task 1 (Section 2) and Task 3

def select_op(choice):
    if choice == '+':
        num1 = input("Enter first number: ")
        print(num1)
        
        if num1.replace('.', '').isdigit():
            num2 = input("Enter second number: ")
            print(num2)
            
            if num2.replace('.', '').isdigit():
                num1 = float(num1)
                num2 = float(num2)
                print(f"{num1:.1f} + {num2:.1f} = {(add(num1, num2)):.1f}")
        
    elif choice == '-':
        num1 = input("Enter first number: ")
        print(num1)
        
        if num1.replace('.', '').isdigit():
            num2 = input("Enter second number: ")
            print(num2)
            
            if num2.replace('.', '').isdigit():
                num1 = float(num1)
                num2 = float(num2)
                print(f"{num1:.1f} - {num2:.1f} = {(subtract(num1, num2)):.1f}")
            else:
                print("Done. Terminating")
                exit()
        
    elif choice == '*':
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        if num1.replace('.', '').isdigit() and num2.replace('.', '').isdigit():
            num1 = float(num1)
            num2 = float(num2)
            print(f"\n{num1:.1f} * {num2:.1f} = {(multiply(num1, num2)):.1f}")
        else:
            print("Not a valid number, please enter again")
    elif choice == '/':
        num1 = input("Enter first number: ")
        print (num1)
        num2 = input("Enter second number: ")
        print (num2)
        if num1.replace('.', '').isdigit() and num2.replace('.', '').isdigit():
            num1 = float(num1)
            num2 = float(num2)
            result = divide(num1, num2)
            if result is not 0:
                print(f"{num1:.1f} / {num2:.1f} = {result:.1f}")
            else:
                print(f"{num1:.1f} / {num2:.1f} = None")
        
    elif choice == '^':
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        if num1.replace('.', '').isdigit() and num2.replace('.', '').isdigit():
            num1 = float(num1)
            num2 = float(num2)
            print(f"{num1:.1f} ^ {num2:.1f} = {(power(num1, num2)):.1f}")
        else:
            print("Not a valid number, please enter again")
    elif choice == '%':
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        if num1.replace('.', '').isdigit() and num2.replace('.', '').isdigit():
            num1 = float(num1)
            num2 = float(num2)
            result = remainder(num1, num2)
            if result is not None:
                print(f"{num1:.1f} % {num2:.1f} = {result:.1f}")
        else:
            print("Not a valid number, please enter again")
    elif choice == '#':
        return -1
    elif choice == '$':
        print("Resetting...")
        return 0
    else:
        print("Unrecognized operation")

#End the select_op(choice) function here
#-------------------------------------

#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
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
    

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if select_op(choice) == -1:
        #program ends here
        print("Done. Terminating")
        exit()


