from itertools import combinations
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    mbti = list(input().split())

    if n > 16**2:
        print(0)
        continue
    threes = tuple(combinations(mbti, 3))
    answer = 1e9

    for three in threes:
        answer = min(answer, len(set(three[0]) - set(three[1])) + len(set(three[1]) - set(three[2])) + len(set(three[0]) - set(three[2])))
        
    print(answer)