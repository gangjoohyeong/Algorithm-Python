from sys import stdin
input = stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
sushi = sushi * 2
answer = 0 

for i in range(n):
    answer = max(answer, len(set(sushi[i:i+k] + [c])))

print(answer)