# https://www.acmicpc.net/problem/16967
from sys import stdin

h, w, x, y = map(int, stdin.readline().split())
a = [[] for _ in range(h)]
print(f"a: {a}")

for i in range(h):
    row = list(map(int, stdin.readline().split()))
    if i < x:
        a[i].extend(row[:w])
        print(f"{i}번째 row: {a}")
    elif x <= i < h:
        a[i].extend(row[:y])
        print(f"{i}번째 row: {a}")
        a[i].extend([(b - a) for b, a in zip(row[y:w], a[i-x][:w-y])])
        print(f"{i}번째 row: {a}")

for a_ in a:
    print(*a_)