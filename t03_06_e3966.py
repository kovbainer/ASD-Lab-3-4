import sys


def contains(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return True
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    m = int(data[1 + n])
    queries = data[2 + n:2 + n + m]
    out = ["YES" if contains(a, int(q)) else "NO" for q in queries]
    sys.stdout.write("\n".join(out) + "\n")


main()
