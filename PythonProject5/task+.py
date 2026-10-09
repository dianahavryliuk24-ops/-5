message = input("Введіть повідомлення (I love Python): ")
result = ""
for char in message:
    lower_char = char.lower()
    if lower_char == 'a':
        result += '1'
    elif lower_char == 'e':
        result += '2'
    elif lower_char == 'i':
        result += '3'
    elif lower_char == 'o':
        result += '4'
    elif lower_char == 'u':
        result += '5'
    else:
        result += char

print(f"\nЗашифроване повідомлення:\n{result}")