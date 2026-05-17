text = input("Введите строку без пробелов: ")

if text == text[::-1]:
    print("Yes")
else:
    print("No")