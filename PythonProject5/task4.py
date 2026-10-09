phone = input("Введіть номер телефону: ")
clean_phone = phone.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
print(f"\nРезультат:\n{clean_phone}")
if clean_phone.startswith("+380"):
    print("Номер починається із +380")
else:
    print("Номер НЕ починається із +380")