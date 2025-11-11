m = int(input("Enter a mark between 0 to 100 for student result: "))

if 0 <= m <= 100:
    if m >= 90:
        print("A++")
    elif 80 <= m < 90:
        print("A+")
    elif 70 <= m < 80:
        print("A")
    elif 60 <= m < 70:
        print("1st class")
    elif 50 <= m < 60:
        print("2nd class")
    elif 33 <= m < 50:
        print("Pass")
    else:
        print("Fail")
else:
    print("Please enter marks between 0 to 100")
