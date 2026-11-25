def f(x):
    return x * x + x ** 0.5


def solve(c):
    lo, hi = 0.0, max(1.0, c ** 0.5)
    for _ in range(100):
        mid = (lo + hi) / 2
        if f(mid) < c:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


c = float(input())
print("%.10f" % solve(c))
