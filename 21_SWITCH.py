# python is not support switch case 

def addition():
    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))
    print(f"Your Addition is {a + b}")

def subtraction():
    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))
    print(f"Your Subtraction is {a - b}")

def multiplication():
    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))
    print(f"Your Multiplication is {a * b}")

def division():
    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))
    if b != 0:
        print(f"Your Division is {a / b}")
    else:
        print("Division by zero is not allowed!")

def default_case():
    print("Please choose a valid option.")

# Display menu
print("Choose any one:\n")
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
x = int(input("Choose your option: "))

# Mimic switch-case using a dictionary
switch = {
    1: addition,
    2: subtraction,
    3: multiplication,
    4: division
}

# Execute the selected function or default case
switch.get(x, default_case)()