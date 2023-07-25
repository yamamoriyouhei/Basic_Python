import math
def trapezoidal_integral(f, a=0, b=1, n=100):
    h = (b - a) / n
    line = 0
    for i in range(n + 1):
        x = a + i * h
        if i == 0 or i == n:
            line += f(x)
        else:
            line  =  line + 2 * f(x)

    line =  line * h / 2
    return line

result1 = trapezoidal_integral(math.sin, 0, math.pi/2, 100)
print("(1) 関数 sin(x) の台形積分結果:", result1)

result2 = trapezoidal_integral(lambda x:4/(1+ x**2), 0, 1, 100)
print("(2) 関数 4/(1+x**2) の台形積分結果::", result2)

result3 = trapezoidal_integral(lambda x: math.sqrt(math.pi)*math.exp(-x**2), -100, 100, 1000)
print("(3) 関数 √π*e^(-x^2) の台形積分結果:", result3)

