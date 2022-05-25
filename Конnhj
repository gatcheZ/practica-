def distance_between_points(x1: float, y1: float, x2: float, y2: float) -> (float):
    res = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return res


sides_in_array = []


def coordinates_to_side():
    a_x = float(input("1 точка стороны А= "))
    a_y = float(input("2 точка стороны А= "))
    b_x = float(input("1 точка стороны В= "))
    b_y = float(input("2 точка стороны В= "))
    c_x = float(input("1 точка стороны C= "))
    c_y = float(input("2 точка стороны C= "))

    side1 = distance_between_points(a_x, a_y, b_x, b_y)
    side2 = distance_between_points(b_x, b_y, c_x, c_y)
    side3 = distance_between_points(c_x, c_y, a_x, a_y)

    sides_in_array.append(side1)
    sides_in_array.append(side2)
    sides_in_array.append(side3)

    return sides_in_array


def triangle_exists_or_not(side1: float, side2: float, side3: float):
    semi_pyrimither = float((side1 + side2 + side3) / 2)
    square = (semi_pyrimither * (semi_pyrimither - side1) * (semi_pyrimither - side2) * (
                semi_pyrimither - side3)) ** 0.5
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        return square
    else:
        return -1


triangles = []
for i in range(1):
    triangles.append(coordinates_to_side())
print(triangles)
for triangle in triangles:
    area = triangle_exists_or_not(triangle[0], triangle[1], triangle[2])
    if area < 0:
        print("треугольник не существует")
#    else:
#        print(area)
sides_in_array.sort()
a = sides_in_array[0]
b = sides_in_array[1]
c = sides_in_array[2]
# def largest_number():



if a**2 + b**2 == c**2:
    print("Он прямоугольный и его площадь:  ")
    print(triangle_exists_or_not(triangle[0], triangle[1], triangle[2]))

else:
    print("no")
