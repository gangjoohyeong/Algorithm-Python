from sys import stdin           # 그냥 input 쓰면 시간 초과
import heapq

n = int(stdin.readline())
h = [] # heap

for _ in range(n):
    x = int(stdin.readline())
    if x > 0:                   # x > 0: 배열에 x 추가
        heapq.heappush(h, x)
    elif x == 0:                # x = 0: pop 프린트 
        if len(h) == 0:
            print(0)            # q 비어있으면 0 프린트 
        else:
            print(heapq.heappop(h))