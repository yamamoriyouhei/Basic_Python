from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math
a = 0
b = math.pi/2
n = 100
h = (b - a) / n
line = 0

for i in range(1, n):
    x_i = a + i * h
    Y = sin(x_i)
    line = line + 2*Y

area = line * h / 2

print("sin関数の積分値の近似値は:", area)