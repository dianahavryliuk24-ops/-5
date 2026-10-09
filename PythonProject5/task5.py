password = input("Введіть пароль: ")
is_long = len(password) >= 8
has_digit = False
has_upper = False
has_lower = False
has_space = False
for char in password:
    if char.isdigit():
        has_digit = True
    elif char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char == " ":
        has_space = True
print()
if is_long and has_digit and has_upper and has_lower and not has_space:
    print("Пароль надійний")
else:
    print("Пароль ненадійний:")
    if not is_long:
        print("- менше 8 символів")
    if not has_digit:
        print("- немає цифри")
    if not has_upper:
        print("- немає великої літери")
    if not has_lower:
        print("- немає маленької літери")
    if has_space:
        print("- містить пробіли")