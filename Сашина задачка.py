name_tovar = 'Ноутбук'
coin = 0

popupka = {
    "Попыт": 6,
    "Микроволновка": 8,
    "Ноутбук": 82
}
object = {
    "Ноутбук": {
        "Стоимость товара": 99000,
        "Остаток на складе": 0,
        "Категория товара": "Электроника"
    },
    "Смартфон": {
        "Стоимость товара": 20000,
        "Остаток на складе": 8,
        "Категория товара": "Электроника"
    },
    "Холодильник": {
        "Стоимость товара": 40000,
        "Остаток на складе": 9,
        "Категория товара": "Бытовая техника"
    }
}


def 云克苏(spisok: dict):
    for price, amount in spisok.items():
        print("." * 20)
        print(f"Наименование товара {price!r}")
        print("-" * 20)
        for object_name, kinds in amount.items():
            print(f"{object_name} - {kinds}")


def bubuyka(spisok: dict, tovar: str):
    if tovar in spisok:
        global coin
        if spisok[tovar]["Остаток на складе"] <= 0:
            print("Товара нет на складе")
        else:
            coin = coin + spisok[tovar]["Стоимость товара"]
            spisok[tovar]["Остаток на складе"] = spisok[tovar]["Остаток на складе"] - 1
            print(f"В кассе есть - {coin} руб.")
    else:
        print("Такого товара нет")


def popupki(chto_pokupaem: dict, spisok: dict):
    global coin
    for kind, count in chto_pokupaem.items():
        if kind in spisok.keys():
            if spisok[kind]["Остаток на складе"] < count:
                in_stock = spisok[kind]["Остаток на складе"]
                price = count * in_stock
                coin += spisok[kind]["Остаток на складе"] * spisok[kind]["Стоимость товара"]
                spisok[kind]["Остаток на складе"] = 0
                print(f"Вы купили {kind}, {in_stock} предмета, потому что больше нет, и стоило это {price} денег")
            else:
                price_1 = count * spisok[kind]["Стоимость товара"]
                coin += price_1
                spisok[kind]["Остаток на складе"] -= count
                print(f"Вы купили {kind}, {count} предмета, и стоило это {price_1} денег")

            # 云克苏(spisok)
            print(f"В кассе у нас {coin} денег ")
        else:
            print(f"Ты не сможешь купить {kind}, у нас такого нет, иди отсюда")


# bubuyka(object, "qwe")
# print(object)
# popupki(popupka, object)


def 妓女(spisok: dict, tovar: str):
    if tovar not in spisok:
        print("Иди отсюда пес, такого нет")
        return
    for name, glossary in spisok.items():
        if spisok[tovar]["Категория товара"] == glossary["Категория товара"]:
            analog = dict()
            kat = glossary["Категория товара"]
            if spisok[tovar]["Стоимость товара"] > glossary["Стоимость товара"]:
                print(f"Товар {name} дешевле чем {tovar}, он также относится к категории {kat}")
                analog[name] = glossary
                return 云克苏(analog)
            else:
                print(f"Нет ничего дешевле {tovar} в категории {kat}")


# 妓女(object, "Ноутбук")

def refill(spisok: dict, tovarui: dict):
    for kind, remainder in tovarui.items():
        if kind in spisok.keys():
            spisok[kind]["Остаток на складе"] += remainder
        else:
            spisok[kind] = dict()
            spisok[kind]["Остаток на складе"] = remainder
    return 云克苏(spisok)


refill(object, popupka)
