# Задача 1
coor_f = input("Введите координаты первой точки: ")
coor_s = input("Введите координаты второй точки: ")
x_f, y_f = coor_f.split()
x_s, y_s = coor_s.split()
x_f, y_f = float(x_f), float(y_f)
x_s, y_s = float(x_s), float(y_s)
print(f"Расстояние между точками равно: {(((x_s - x_f)**2)+((y_s-y_f)**2))**0.5}")

-----------------------------------------------------------------------------------------------------
# Задача 2
znal_list = input("Введите символ листвы: ")
kol_znak_list= len(znal_list)
if kol_znak_list > 1:
    print("Ошибка! Необходимо ввести ровно один символ")
else:
    znak_osnov = input("Введите сивмол основания: ")
    kol_znal_osnov = len(znak_osnov)
    if kol_znal_osnov > 1:
        print("Ошибка! Необходимо ввести ровно один символ")
    else:
        height= int(input("Введите высоту ёлочки: "))
        height_osnov= int(input("Введите высоту основания: "))
        weight_osnov= int(input("Введите толщину основания: "))   
i_height=1
cen =1
cene=height*2
while i_height<=height:
    print((znal_list*cen).center(cene, " "))
    cen+=2
    i_height+=1
i_osnov=1
while i_osnov<=height_osnov:
    print((znak_osnov*weight_osnov).center(height*2))
    i_osnov+=1
    
-----------------------------------------------------------------------------------------------------
# Задача 3
string = input("Введите строку: ")
string_f = string.replace(" ", "")
string_s = string_f
string_s=string_s[::-1]
string_f= string_f.lower()
string_s= string_s.lower()
print(string_f)
print(string_s)
if string_f == string_s:
    print("Эта строка является палиндромом")
else:
    print("Это не палиндром")
    
-----------------------------------------------------------------------------------------------------    
# Задача 4
num = int(input("Введите число: "))
summa=int(0)
while num!=0:
    w = num % 10
    summa=summa+w
    num=num//10
print(f"Сумма = {summa}")
