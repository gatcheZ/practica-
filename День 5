-------------------------------------------------------------
# задание 1

a = float(input("первое число= "))
b = float(input("второе число= "))
c = float(input("третье число= "))
d = float(input("четвертое число= "))
e = float(input("пятое число= "))
f  = float(input("шестое число= "))
def roots(a: float, b: float, c: float, d: float) -> (float):
     res = ((b - a)**2 + (d + c)**2)**0.5
     return res
side1=roots(a,b,c,d)
side2=roots(c,d,e,f)
side3=roots(e,f,a,b)
poluper=float((side1+side2+side3)/2)
plochad=float((poluper*(poluper - side1)*(poluper - side2)*(poluper - side3))**0.5)
if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
    print(f"Такой треугольник существует, его площадь равна= {plochad:.3}")
else:
    print("Такого треугольника не существует")
