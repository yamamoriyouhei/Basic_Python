a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
def great(a, b):
    while b != 0:
        a, b = b, a % b
    if(a != 1):
        print("a, bの最大公約数は", a)
def disjoint(a,b):
    while b != 0:
        a, b = b, a%b
    if (a == 1):
        print("a,bは互いに素である。")

disjoint(a,b)
great(a, b)
