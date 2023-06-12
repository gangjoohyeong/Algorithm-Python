import sys
from collections import deque
input = sys.stdin.readline

s = input()
t = input()
q = deque()
q.append(s)
answer = 0
print(q)
print(t)
while q:
    s = q.popleft()
    print(s, t)
    if s == t:
        answer = 1
        print('정답')
        break
    elif len(s) == len(t): # q 비울 때까지 더이상 append 안 함 
        continue

    # 만들 가능성 있음
    if s + 'A' in t:
        q.append(s + 'A')
    if 'B' + s[::-1] in t:
        q.append('B' + s[::-1])

print(answer)