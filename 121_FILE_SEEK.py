# FILE READ BY SEEK()

f = open("seek.txt")
f.seek(6, 0)
lines = f.readlines()
for i in lines:
    print(i)
f.close()