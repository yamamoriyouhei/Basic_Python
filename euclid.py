a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
def disjoint(a, b):
    while b != 0:
        a, b = b, a % b

    if a == 1:
        print("a, bは互いに素です")
    else:
        print("a, bの最大公約数は", a)

disjoint(a, b)
