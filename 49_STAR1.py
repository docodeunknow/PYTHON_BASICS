n = int(input("Enter the number: "))

for i in range(1, n + 1):       # Outer loop for rows
    for j in range(1, i + 1):   # Inner loop for columns
        print("*", end="")      # Print stars on the same line
    print()                     # Move to the next line after each row
