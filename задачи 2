https://github.com/stinger000/Practice_2022/blob/main/Day%204/4.1.py
____________________________________________________________________________
# print("Введите коэффициенты квадратного уравнения:")


def roots(a: float, b: float, c: float) -> (bool, float, float):
    x1 = 0
    x2 = 0
    
    descrim = float((b**2) - 4*a*c)
    if descrim < 0:
        print(f"нет решений")
        return False, x1, x2
    elif descrim == 0: 
        x1 = -b/ 2*a
        x2 = -b/ 2*a
        return True, x1, x2
    elif descrim > 0:
        x1 = (-b + (descrim)**0.5)/2 * a
        x2 = (-b - (descrim)**0.5)/2 * a
        return True, x1, x2
        print(f"первый корень: {x1}, второй корень{x2}")
print(roots(1,-5,6))
______________________________
# задача номер 1


# print("Введите коэффициенты квадратного уравнения:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

def roots(a: float, b: float, c: float) -> (bool, float, float):
    x1 = 0
    x2 = 0
    
    descrim = float((b**2) - 4*a*c)
    if descrim < 0:
        return False, x1, x2
    elif descrim == 0: 
        x1 = -b/ 2*a
        x2 = -b/ 2*a
        return True, x1, x2
    elif descrim > 0:
        x1 = (-b + (descrim)**0.5)/2 * a
        x2 = (-b - (descrim)**0.5)/2 * a
        return True, x1, x2
# print(roots(a,b,c))

danet, otvet1, otvet2 = roots(a, b, c)
# print(f"{danet= }, {otvet1= } , {otvet2= }")
if danet == False:
    print("реший нет ты овощ")
else:
    print(f"корни уравнения: {otvet1} , {otvet2}")

