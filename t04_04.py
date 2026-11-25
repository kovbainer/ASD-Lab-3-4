from math import sin


def f(x):
    return sin(x) - x / 3


def bisection(f, a, b, eps=1e-12):
    while b - a > eps:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return (a + b) / 2


x = bisection(f, 1.6, 3)
print("x = %.6f" % x)
print("f(x) =", f(x))
