# FILE BINARY READ AND WRITE

# list = [20, 30, 40]
# # WRITE

# f = open("binary.txt", "wb")
# arr = bytearray(list)
# f.write(arr)
# f.close()

# READ 

f = open("binary.txt", "rb")
num = list(f.read())
print(num)
f.close()
