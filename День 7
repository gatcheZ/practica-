# def sep():
#     print("-"*120)

# задание 1
user_name = input("Какое блюдо удалить: ")
# user_number_product = int(input("Какой элемент вывести: "))

evg_products = ["Цезарь", "Краб", "Оливье"]
ivan_products = ["Шаурма", "Сэндвич", "Шашлык"]
all_products = evg_products + ivan_products
print(all_products)

# new_product = all_products[:user_number_product]
# print(new_product)
# sep()
# задание 2
if user_name in all_products:
    all_products.remove(user_name)
    print(f"{user_name} удален из списка")
    print(all_products)
else:
    print(f"{user_name} нет в списке")
-----------------------------------------------------------------------------------
evg_products = ["Цезарь", "Краб", "Оливье"]
ivan_products = ["Шаурма", "Сэндвич", "Шашлык"]
all_products = evg_products + ivan_products
products_count = len(all_products)
print(f"В моем списке есть {products_count} продуктов")


for i in range(products_count):
    print(f"Я люблю {all_products[i]}")

-----------------------------------------------------------------------------------
numbers = []
for i in range(5):
    number = int(input("Введите число: "))
    numbers.append(number)


list_count = len(numbers)
# print(f"Всего {list_count} чисел")
minimum = numbers[0]
maximum = numbers[0]
for i in range(list_count):
    if minimum < numbers[i]:
        maximum = numbers[i]
    elif maximum > numbers[i]:
        minimum = numbers[i]
print(minimum,maximum)
