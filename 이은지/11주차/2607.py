# https://www.acmicpc.net/problem/2607
# 조건 1.  
# 조건 2.
from sys import stdin 
from collections import Counter

k = int(stdin.readline())
target = stdin.readline()
target_cnt = Counter(target)
answer = 0

for _ in range(k-1):
    word = stdin.readline()
    word_cnt = Counter(word)
    
    if len(target) - len(word) not in range(-1, 2):
        continue

    sub1 = sum(list((target_cnt - word_cnt).values()))
    sub2 = sum(list((word_cnt - target_cnt).values()))

    # 같은 구성을 갖는 경우 
    if target_cnt == word_cnt:
        answer += 1
    # 하나 바꿔서 같은 구성이 되는 경우 
    elif sub1 == 1 and sub2 <= 1:
        answer += 1
    elif sub2 == 1 and sub1 <= 1:
        answer += 1

print(answer)