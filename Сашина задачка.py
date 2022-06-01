name_tovar = 'Ноутбук'
coin = 0


popupka = {
    "Попыт": 6,
    "Микроволновка": 8,
    "Ноутбук": 2
}
object = {
    "Ноутбук": {
        "Стоимость товара": 99000,
        "Остаток на складе": 5,
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
        print("朗道" * 20)
        print(f"Наименование товара {price!r}")
        print("화준" * 20)
        for object_name, kinds in amount.items():
            print(f"{object_name} - {kinds}")

def bubuyka(spisok: dict, tovar: str):
    if tovar in spisok:
        global coin
        coin = coin + spisok[tovar]["Стоимость товара"]
        spisok[tovar]["Остаток на складе"] = spisok[tovar]["Остаток на складе"] - 1
        print(f"В кассе есть - {coin} руб.")
    else:
        print("Такого товара нет")

def popupki(chto_pokupaem:dict,spisok: dict):
    global coin
    for kind, count in chto_pokupaem.items():
        if kind in spisok.keys():
            if spisok[kind]["Остаток на складе"] < chto_pokupaem[count]:
                coin += spisok[kind] * chto_pokupaem[kind]["Стоимость товара"]
                spisok[kind]["Остаток на складе"] = 0
            else:
                coin += count * chto_pokupaem[kind]["Стоимость товара"]
                spisok[count] -= count

            print(coin)
            云克苏(spisok)
        else:
            print("у нас такого нет, иди отсюда")
popupki(popupka, object)




# if __name__ == 'main':
    # bubuyka(object, name_tovar)
    # 云克苏(object)
    # popupki(popupka, object)
