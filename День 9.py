 # задача 0
 num = []

for i in range(5):
    input_numbers = int(input("Введите число: "))
    num.append(input_numbers)


def numbers(plus_num):
    for num in plus_num:
        if num > 0:
            print(num)


numbers(num)
---------------------------------------------------------------------------------------------------
