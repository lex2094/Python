
a = int(input())
b = int(input())
if b != 0:
    print(a/b)
else:
    print("деление невозможно")
    b = int(input('введите ненулевое значение '))
    if b == 0:
        print("опять ноль")
    else:
        print(int(a/b))

