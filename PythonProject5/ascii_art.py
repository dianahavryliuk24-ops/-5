n = int(input("Введіть розмір фігури N: "))

print("\n1. Квадрат")
for i in range(n):
    print("*" * n)

print("\n2. Прямокутний трикутник")
for i in range(1, n + 1):
    print("*" * i)

print("\n3. Перевернутий трикутник")
for i in range(n, 0, -1):
    print("*" * i)

print("\n4. Піраміда")
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

print("\nДодатково: порожня піраміда (рамка)")
for i in range(1, n + 1):
    spaces = " " * (n - i)
    if i == 1:
        print(spaces + "*")
    elif i == n:
        print("*" * (2 * n - 1))
    else:
        print(spaces + "*" + " " * (2 * i - 3) + "*")