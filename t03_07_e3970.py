import sys


def lower_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    m = int(data[1 + n])
    queries = data[2 + n:2 + n + m]
    out = []
    for q in queries:
        x = int(q)
        out.append(str(upper_bound(a, x) - lower_bound(a, x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
