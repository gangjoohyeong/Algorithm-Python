# 햄버거 분배 https://www.acmicpc.net/problem/19941
from sys import stdin

n, k = map(int, stdin.readline().split())
HP = stdin.readline()
cnt = 0
visited = []

for index, value in enumerate(HP):
    if value == 'P':
        for i in range(-k, k+1):
            loc = index + i
            if loc < 0 or loc >= len(HP):
                continue
            if HP[loc] == 'H' and loc not in visited:
                cnt += 1
                visited.append(loc)
                break

print(cnt)