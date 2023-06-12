# https://www.acmicpc.net/problem/17086
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

answer = 0

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, -1, -1, -1]

q = deque()
for i in range(n):
    for j in range(m):
            if graph[i][j] == 1: # 상어 있으면
                 q.append((i, j)) # 위치 저장

while q:
     x, y = q.popleft() # 상어 있는 위치
     for i in range(8):
          nx, ny = x + dx[i], y + dy[i]
          if nx < 0 or nx >= n or ny < 0 or ny >= m:
               continue
          if graph[nx][ny] == 0:
               q.append((nx, ny))
               graph[nx][ny] = graph[x][y] + 1
               answer = max(answer, graph[nx][ny])

print(answer - 1)