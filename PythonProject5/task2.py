text = input("Введіть текст: ")
vowels_count = 0
for char in text.lower():
    if char in "aeiou":
        vowels_count += 1
print(f"\nКількість голосних: {vowels_count}")