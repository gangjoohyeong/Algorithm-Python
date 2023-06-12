# 쉬운 최단거리
from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:    # 목표지점
            q.append((i, j))    # 위치 저장
            
while q:
    x, y = q.popleft()
    # answer = graph[x][y]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1:
            q.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

for row in graph:
    row = list(map(lambda x: x-2 if x > 0 else 0, row))
    print(' '.join(map(str, row)))
