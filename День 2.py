# Задача 1
cel = int(input("Введите температуру в градусах цельсия:"))
kul = float(cel+273)  
far = float(cel*9/5+32) 
result = f"{cel} в градусах цельсия это - {kul} в градусах кельвина или {far} градусов фарингейта"
print(result)

-----------------------------------------------------------------------------------------------------
# Задача 2
age = int(input("Введите ваш возраст:" ))
if age>=18:
    print("Вы можете получить права")
else:
    new_years=int(2022+(18-age))
    result= f"Вы можете получить права в {new_years} году "
    print(result)
    
-----------------------------------------------------------------------------------------------------
# Задача 3
num1= int(input("Первое число: "))
num2= int(input("Второе число: "))
num3= int(input("Третье число: "))
if num2<num1>num3:
    print("Наибольшее число", num1)
elif num1<num2>num3:
    print("Наибольшее число", num2)
elif num1<num3>num2:
    print("Наибольшее число", num3)

if num2>num1<num3:
    print("Наибольшее число", num1)
elif num1>num2<num3:
    print("Наибольшее число", num2)
elif num1>num3<num2:
    print("Наименьшее число", num3)
    
-----------------------------------------------------------------------------------------------------
# Задача 4
side1=float(input("Первая сторона: "))
side2=float(input("Вторая сторона: "))
side3=float(input("Третья сторона: "))
poluper=float((side1+side2+side3)/2)
plochad=float((poluper*(poluper - side1)*(poluper - side2)*(poluper - side3))**0.5)
if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
    print(f"Такой треугольник существует, его площадь равна{plochad:.3}")
else:
    print("Такого треугольника не существует")
    
-----------------------------------------------------------------------------------------------------
# Задача 5
num1= int(input("Первое число: "))
znak= str(input("Знак выражения: "))
num2= int(input("Второе число: "))
if znak == "*":
    print(num1 * num2)
elif znak == "+":
    print(num1 + num2)
elif znak == "/":
    print(num1 / num2)
elif znak == "-":
    print(num1 - num2)
    
elif znak == "**":
    print(num1 ** num2)
    
-----------------------------------------------------------------------------------------------------
# Задача 6
length_steb = int(input("Длина стебля: "))
length_up = int(input("На сколько поднимается: "))
length_down = int(input("На сколько спускается: "))
length_now = 0
i = 0
while length_now != length_steb:
    if length_up>length_down:
        length_now = length_now + length_up - length_down
        i += 1
    else:
        print("Коровка никогда не поднимется")
        break
print(f"{i} дней поднималась коровка")    
