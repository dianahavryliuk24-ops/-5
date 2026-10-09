text = input("Введіть текст: ")
print(f"\n1. Початковий текст: {text}")
print(f"2. Кількість усіх символів: {len(text)}")
words = text.split()
print(f"3. Кількість слів: {len(words)}")
letters = digits = vowels = 0
for char in text:
    if char.isalpha():
        letters += 1
    if char.isdigit():
        digits += 1
    if char.lower() in "aeiou":
        vowels += 1
print(f"4. Кількість літер: {letters}")
print(f"5. Кількість цифр: {digits}")
print(f"6. Кількість голосних: {vowels}")
print(f"7. Текст у нижньому регістрі: {text.lower()}")
print(f"8. Текст у верхньому регістрі: {text.upper()}")
python_count = text.lower().count("python")
print(f"9. Кількість входжень слова Python: {python_count}")
print(f"10. Зворотний порядок: {text[::-1]}")