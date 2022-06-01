# Задача 1
name = input("Введите имя: ")
age = int(input("Введите ваш возраст: "))
year = int (input("Введите год: "))
new_age = int(year - 2022 + age)
print(f"Привет, {name} в {year} году тебе будет {new_age} лет")
