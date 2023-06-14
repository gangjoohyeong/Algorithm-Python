# https://www.acmicpc.net/problem/9205
from sys import stdin 
from collections import deque

def bfs():
    q = deque()

    # 출발 지점 
    q.append([start[0], start[1]])

    while q:
        x, y = q.popleft()
        if abs(x-end[0]) + abs(y-end[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                xi, yi = store[i]
                if abs(xi-x) + abs(yi-y)<= 1000:
                    q.append([xi, yi]) 
                    visited[i] = True
    print("sad")
    return
                

t = int(stdin.readline())
# 갈 수 있는 곳: 거리가 1000 이하 

for _ in range(t):
    n = int(stdin.readline()) # 편의점 개수 
    visited = [False for _ in range(n+1)]
    # 상근이 집
    start = list(map(int, stdin.readline().split()))
    # 편의점
    store = [list(map(int, stdin.readline().split())) for _ in range(n)]
    # 락페 
    end = list(map(int, stdin.readline().split()))
    bfs()