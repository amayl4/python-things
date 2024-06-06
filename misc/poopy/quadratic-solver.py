# basic quadratic equation solution

def solveQE(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("Equation has no real roots")
    elif discriminant == 0:
        x = (-1*b) / (2*a)
        print("Repeated root at x = ", x)
    elif discriminant > 0:
        x1 = (1*b + discriminant**0.5) / 2*a
        x2 = (1*b - discriminant**0.5) / 2*a
        print("Roots are ", x1, " and ", x2)

solveQE(1, 4, 4)