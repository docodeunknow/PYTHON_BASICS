cn = int(input("Enter a customer number  : "))
u =  int(input("Enter the Unit :"))

if u <=200:
    c = 0.5 * u
elif u <=400:
    c = 100 + 0.65 * (u-200)
elif u <=600:
    c = 230 + 0.80 * (u-400)
else:
    c = 390 + (u-600)

print(f"customer number : {cn} ")
print(f"Charget :{c}")
