while True:
    cmd=input("Выберите один из знаков> ")
    if cmd=="exit":
        break
    elif cmd =="/":
        a = int(input())
        b = int(input())
        print(a / b)
