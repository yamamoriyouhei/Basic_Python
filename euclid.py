a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
while b != 0:
    a, b = b, a%b
print("aとbの最大公約数は",a)
