text = input("Введіть текст: ")
letters = digits = spaces = others = 0
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    else:
        others += 1
print(f"\nЛітер: {letters}")
print(f"Цифр: {digits}")
print(f"Пробілів: {spaces}")
print(f"Інших символів: {others}")