import math

def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)

    return x1, x2
x1, x2 = quadratic_equation(1, -6, 9)
print("(1): x1 =", x1, ", x2 =", x2)

x1, x2 = quadratic_equation(1, 2, -8)
print("(2): x1 =", x1, ", x2 =", x2)

x1, x2 = quadratic_equation(8, -6, -35)
print("(3): x1 =", x1, ", x2 =", x2)

x1, x2 = quadratic_equation(1, 0, 1)
print("(4): x1 =", x1, ", x2 =", x2)
