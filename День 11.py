food = {
    "Салат": {
        "Мужские слезы": 555,
        "Красное море": 665,
        "Моя прекрасная леди": 325,
        "Ёжик": 125,
        "Цезарь": 329,
        "Оливье": 440
    },

    "Супы": {
        "Куриный суп": 300,
        "Сырный суп": 590,
        "Затируха": 362,
        "Гречневый суп": 532,
        "Томатный рисовый суп": 783
    },

    "Напитки": {
        "Пиво": 150,
        "Вино": 180,
        "Липтон": 100,
        "Кофе с кокосиком": 220
    }

}

# clients_food = str(input("Введите название блюда: "))
clients_category = str(input("Введите название категории: "))


# задание 0.5

def food_exist(q: str):
    for dish in food.values():
        if q in dish:
            return True
    return False


# задание 0.6

def kind_of_food(kind_food: str):
    for kind, dish in food.items():
        if kind_food in dish:
            return kind

    print("net")
    return False


# задание 1

# print(food_exist(clients_food))
# print(kind_of_food(clients_food))

def category(clients_category: str):
    if clients_category in food:
        print(sum(food[clients_category].values()))
        return True
    else:
        return False


# print(category(clients_category,food))

# задание 2

def add_food(clients_category: str):
    if category(clients_category) == True:
        name_food = str(input("Введите новый продукт: "))
        callor_food = int(input("Введите калорийность этого продукта: "))
        food[clients_category][name_food] = callor_food

# (add_food(clients_category))
# print(food)


# задание 3

def add_category():
    new_category = str(input("Введите название новой категории: "))
    food[new_category] = dict()
add_category()
print(food)

# задание 4

for kind, dish in food.items():
    print("-"*70)
    print(f"Содержание {kind!r}")
    print("-"*70)
    for food_name, callories in dish.items():
        print(f"В {food_name} - {callories} каллорий")






