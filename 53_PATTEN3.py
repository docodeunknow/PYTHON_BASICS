n = int(input("Enter the number: "))

for i in range(1, n + 1):  # Outer loop starts at 1 and goes up to 5
    for j in range(n + 1 - i):  # Inner loop determines the number of times to print `i`
        print(i, end="")  # Print the number `i` on the same line
    print()  # Move to the next line after each row
