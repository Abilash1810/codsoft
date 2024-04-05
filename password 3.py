# User input for desired password length
N = int(input("Enter the total desired length of your password: "))

# User input for intended password
password = input("Enter your intended password: ")

# Calculate the remaining length needed
remaining_length = N - len(password)

# Define characters for password generation
chars = '1234567890!@#$%^&*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?'

# Generating additional characters to complete the password
for i in range(remaining_length):
    if i == 0:
        # Print the initial password (user input)
        print(password)
    else:
        # Adding a randomly chosen character to the password
        p = secrets.choice(chars)
        password += p

# Print the final generated password
print("Generated password:", password)
