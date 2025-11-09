import math
while True:
    cmd=input("Выберите один из знаков> ")
    if cmd=="exit":
        break
    elif cmd=="степень":
        a=int(input("Введите число,возводимое в степень "))
        b=int(input("Введите степень "))
        print(a**b)
    elif cmd=="косинус":
        a=int(input())
        print(math.cos(a))