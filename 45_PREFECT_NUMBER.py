n = int(input("Enter a number to check if it is 'perfect': "))
original = n
sum_of_digits = 0
product_of_digits = 1

for i in range(n):
    digit = n % 10
    sum_of_digits += digit
    product_of_digits *= digit
    n //= 10

if sum_of_digits == product_of_digits:
    print(f"Your number {original} is 'perfect' based on the sum and product of its digits.")
else:
    print(f"Your number {original} is not 'perfect'.")
