n = int(input("Enter the number: "))

for i in range(n, 0, -1):   # Outer loop starts at `n` and decreases to 1
    for j in range(i):      # Inner loop controls the number of stars per row
        print("*", end="")  # Print stars on the same line
    print()                 # Move to the next line after each row
