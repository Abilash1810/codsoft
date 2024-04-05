import math
# Get user input for two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Display available mathematical operations
print("Mathematical Operations available:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")

# Get user choice for the operation
N = int(input("Choose the operation: "))

# Perform calculations based on user choice
def calculations(a, b):
    if N == 1:
        print("The solution is:", a + b)
    elif N == 2:
        print("The solution is:", a - b)
    elif N == 3:
        print("The solution is:", a * b)
    elif N == 4:
        print("The solution is:", a / b)
    elif N == 5:
        print("The solution is:", a // b)
    else:
        print("Please enter a valid option")

# Call the calculations function
calculations(a, b)