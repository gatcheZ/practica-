# # задача 1----------------------------------------------
multiplication = []
for i in range(11):
    qwe = i * 2
    multiplication.append(qwe)
print(multiplication)
# задача 2----------------------------------------------------
multiplication_on_5 = []
for i in range(11):
    qwe = i * 5
    multiplication_on_5.append(qwe)
print(multiplication_on_5)
# задача 3----------------------------------------------

all = []
for i in multiplication:
    if i in multiplication_on_5:
        all.append(i)
print(all)
# задача 4--------------------------------------------------------
m = 0
summ_of_numbers = 0
for m in all:
    summ_of_numbers+= m
print(f"Их сумма равна {summ_of_numbers}")
#задача 5---------------------------------------------------------
fibanachu1 = 1
fibanachu2 = 0
all = [0]
n = int(input("Введите число: "))
for i in range(n-1):
    fibanachu1,fibanachu2 = fibanachu2, fibanachu1 + fibanachu2
    all.append(fibanachu2)
print(all)  
# задача 6 -------------------------------------------------------------------
from random import randint
a = randint(1,10)
n = int(input("Введите число: "))
while n!= a:
    if n < a:
        print("число меньше того что задумал компьютер")
        n = int(input("Попробуй еще раз: "))
    elif n > a:
        print("число больше чем то что задумал компьютер")
        n = int(input("Попробуй еще раз: "))
    else:
        print("вы угадали!")
print(a)
print(n)
