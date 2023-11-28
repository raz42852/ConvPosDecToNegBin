# קולט מספר חיובי ומספר ביטים
num = int(input("Enter a number : "))
numBytes = int(input("Enter a number of bytes : "))
arr = []

# מאתחל את המערך לרק אפסים עם מספר מקומות של כמות הביטים
for i in range(numBytes):
    arr.append(0)

# מייצג את המספר שנקלט כבינארי ומכניס כל ביט למערך
x = numBytes - 1
while x >= 0:
    arr[x] = num % 2
    num //= 2
    x -= 1

# הופך את כל הספרות לספרה הנגדית שלה
for i in range(numBytes):
    if arr[i] == 0:
        arr[i] = 1
    else:
        arr[i] = 0

# מוסיף למערך 1 מימין
x = numBytes - 1
while x >= 0:
    if arr[x] == 1:
        arr[x] = 0
    else:
        arr[x] = 1
        x = -1
    x -= 1

# יוצר מחרוזת שתכלול את כל הביטים
str_binar_opp = ""
for i in arr:
    str_binar_opp += str(i)

# הדפסה של המספר הבינארי שנקלט כשלילי
print(str_binar_opp)
