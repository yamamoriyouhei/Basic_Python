a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
def prime(number):
    number = int(number)
    for i in range(2,number):
        if number % i ==0:
            return False
    return True
if prime(a):
    print("aは素数です")
else:
    print("aは素数ではありません")
if prime(b):
    print("bは素数です")
else:
    print("bは素数ではありません")