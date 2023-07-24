
import math
a = 0
b = math.pi/2
n = 100
h = (b - a) / n
line = 0
for i in range(n + 1):
    x = a + i * h
    if i == 0 or i == n:
        line += math.sin(x)
    else:
        line  =  line + 2 * math.sin(x)

line =  line * h / 2

print("sin関数の台形積分の近似値は:", line)