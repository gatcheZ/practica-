# задание 1---------------------------------------------------------------

god = int(input("Введите год: "))

def visok_year(god: int) -> (bool):
    if god % 400 == 0 or god % 4 == 0 and god % 100 != 0:
        # print("год высокосный")
        return True
    else:
        # print("год не высокосный")
        return False

# visok_year(god)

# задание 2---------------------------------------------------------------

def daysyear() -> (int):
    if visok_year(god):
        return 366
    else:
        return 365

# print(f"В {god} году {daysyear()} дней")

# задание 3---------------------------------------------------------------

day = int(input("Введите день: "))
month = int(input("Введите месяц: "))

def neotriz(day: int, god: int, month: int) -> (bool):
    if day < 0 or god < 0 or month < 0 or month > 12:
        return False
    else:
        return True

def dney_v_month(day: int, god: int, month: int) -> (int):
    if month == 2:
        if visok_year(god) == True:
            return 29
        else:
            return 28
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month - 1]

def dney_polz_dney_v_month(day: int, god: int, month: int) -> (bool):
    if neotriz(day, god, month) == False:
        print("Неверные значения")
        return False
    dney = dney_v_month(day, god, month)
    if day <= dney:
        print(f"да, такой день существует")
        return True
    else:
        print(f"нет, такого дня не существует")
        return False
        
dney_polz_dney_v_month(day, god, month)




