from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

h = (math.pi/2 - 0) / 100
line = 0

for i in range(1, 100):
    x_i = 0 + i * h
    Y = sin(x_i)
    line = line + 2*Y

area = line * h / 2

print("sin関数の積分値の近似値は:", area)
