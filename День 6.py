# задание 1
my_fav_food = ["цезарь", "пивасик", "кофе"]

# print(f"моя любимая еда это: {my_fav_food[0]}, {my_fav_food[1]}, {my_fav_food[2]}")

minus_food = int(input("Введите номер продукта которы нужно удалить: ")) -1

new_food = str(input("Введите новый продукт: "))


# print(food_count)
# print(f"в моём списке любимых продуктов есть {food_count} позиции:")
def change_food_name(minus_food: int, new_food: str) -> (int, str):
    food_count = len(my_fav_food)
    if minus_food > food_count or minus_food < 0:
        print("Введите коректные значения!")
        return False
    else:
        my_fav_food[minus_food] = new_food
        i = 0
        while i < food_count:
            print(f"я люблю есть {my_fav_food[i]}")
            i += 1



change_food_name(minus_food, new_food )
----------------------------------------------------------------------
# задание 1
my_fav_food = ["цезарь", "пивасик", "кофе"]

# print(f"моя любимая еда это: {my_fav_food[0]}, {my_fav_food[1]}, {my_fav_food[2]}")

minus_food = int(input("Введите номер продукта которы нужно удалить: ")) -1

new_food = str(input("Введите новый продукт: "))

samaa_new_food = str
# print(food_count)
# print(f"в моём списке любимых продуктов есть {food_count} позиции:")
def change_food_name(minus_food: int, new_food: str) :
    food_count = len(my_fav_food)
    if minus_food < 0:
        print("Введите коректные значения!")
        return False
    elif minus_food > food_count:
        my_fav_food.append(new_food)
        i = 0
        while i < len(my_fav_food):
            print(f"я люблю есть {my_fav_food[i]}")
            i += 1
    else:
        
        my_fav_food[minus_food] = new_food
        i = 0
        while i < len(my_fav_food):
            print(f"я люблю есть {my_fav_food[i]}")
            i += 1
change_food_name(minus_food, new_food)
