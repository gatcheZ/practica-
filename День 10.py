number_of_eated_food = int(input("Введите сколько продуктов вы сегодня скушали: "))


favorite_food  = {
    "Пиво": 572,
    "Цезарь": 327,
    "Кофе": 120
}
all_food = favorite_food.keys()
# print(all_food)

# for all_food in favorite_food.keys():
#     print(f"В {all_food} {favorite_food.get(all_food)} каллорий")
calloreis = 0
for i in range(number_of_eated_food):
    food = str(input("Введите еду: "))
    if food in favorite_food.keys():
        print(f"{food} присутсвует в словаре")
        calloreis = calloreis + favorite_food[food]

    else:
        print(f"{food} нет в словаре!")
print(f"Вы скушали продуктов на {calloreis}")



