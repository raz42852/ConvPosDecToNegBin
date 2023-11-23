num = int(input("Enter a number : "))
numBytes = int(input("Enter a number of bytes : "))
arr = []

for i in range(numBytes):
    arr.append(0)

x = numBytes - 1
while x >= 0:
    arr[x] = num % 2
    num //= 2
    x -= 1

for i in range(numBytes):
    if arr[i] == 0:
        arr[i] = 1
    else:
        arr[i] = 0

x = numBytes - 1
while x >= 0:
    if arr[x] == 1:
        arr[x] = 0
    else:
        arr[x] = 1
        x = -1
    x -= 1

str_binar_opp = ""
for i in arr:
    str_binar_opp += str(i)

print(str_binar_opp)
