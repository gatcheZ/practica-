profit = 0
item_from_user = "Ноутбук"
spisok_items = {
    'Ноутбук': 5,
    "Айфон": 5
}

products = {
    "Ноутбук": {
        "price": 99000,  # Цена
        "amount": 5,  # Остаток на складе
        "kind": "Бытовая техника"  # Категория
    },
    "Айфон": {
        "price": 180000,
        "amount": 3,
        "kind": "Предмет роскоши"
    },
    "Телевизор": {
        "price": 45000,
        "amount": 8,
        "kind": "Бытовая техника"
    }
}


def shop(products_dict: dict):
    for kind, item in products_dict.items():
        print("-" * 70)
        print(f"Продукт - {kind!r}")
        print("-" * 70)
        for item_name, keys in item.items():
            print(f" {item_name} - {keys} ")


def purchase_product(item_to_buy: str, products_dict: dict):
    if item_to_buy in products_dict:
        global profit
        if products_dict[item_to_buy]["amount"] <= 0:
            print("Товара нет на складе(")
        else:
            products_dict[item_to_buy]["amount"] -= 1
            profit += products_dict[item_to_buy]["price"]
            print(f"\nПотраченные деньги: {profit}")
    else:
        print("Такого продукта нет(")


def purchase_goods(items_to_buy: dict, products_dict: dict):
    global profit
    for kind, count in items_to_buy.items():
        if kind in products_dict.keys():
            if products_dict[kind]["amount"] < count:
                profit += count * products_dict[kind]["price"]
                products_dict[kind]["amount"] = 0
            else:
                profit += count * products_dict[kind]["price"]
                products_dict[kind]["amount"] -= count

            print(profit)
            shop(products_dict)
        else:
            print("у нас такого нет, иди отсюда")




def recommendations(products_dict: dict, items_to_buy: str):
    if items_to_buy not in products_dict:
        print("Иди отсюда пес, такого нет")
        return
    for name, count in products_dict.items():
        if products_dict[items_to_buy]["kind"] == count["kind"]:
            analog = dict()
            if products_dict[items_to_buy]["price"] > count["price"]:
                kat = products_dict[name]["kind"]
                print(f"Товар {name} дешевле чем {items_to_buy}, он также относится к категории {kat}")
                analog[name] = count
                return shop(analog)
            else:
                print("Нет ничего дешевле данного товара")


recommendations(products, "Ноутбук")

# if __name__ == '__main__':
# purchased_goods(spisok_items, products)
# purchase_product("Ноутбук", products)
