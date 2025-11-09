while True:
    cmd=input("Выберите один из знаков> ")
    if cmd=="exit":
        break
    elif cmd == "+":
        a = int(input())
        b = int(input())
        print(a+b)
    elif cmd=="степень":
        a=int(input("Введите число,возводимое в степень "))
        b=int(input("Введите степень "))
        print(a**b)
    elif cmd=="косинус":
        a=int(input())
        print(math.cos(a))
    elif cmd =="/":
        a = int(input())
        b = int(input())
        print(a / b)
    elif cmd == "*":
        a = int(input())
        b = int(input())
        print(a*b)
    else:
        print("Введен неверный знак действия.")
