class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f"Точка с координатамиx x = {self.x},y = {self.y}"


def print_x_y(prod: Point):
    print(f"это {prod.x} и {prod.y} ")



def input_x_y() -> Point:

    x = input("Введите первое число: ")
    y = input("Введите второе число: ")
    p = Point(x, y)
    return p

print(input_x_y())

