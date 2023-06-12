# https://www.acmicpc.net/problem/4485
from sys import stdin
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 1
INF = int(1e9)

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))              # q에 (우선순위, 값) 을 push
    distance[0][0] = 0                                  # 시작 노드 초기화 

    while q:                                            # q가 비어있을 때까지 반복
        now_cost, now_x, now_y = heapq.heappop(q)       # 우선순위가 가장 작은 값 (가장 작은 루피) pop

        if now_x == (n-1) and now_y == (n-1):           # 도착지 도착
            print(f"Problem {cnt}: {distance[n-1][n-1]}")
            break

        for i in range(4):
            x = now_x + dx[i]
            y = now_y + dy[i]
            # 범위를 벗어남
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            # 그래프 내부
            cost = now_cost + graph[x][y]
            if cost < distance[x][y]:
                distance[x][y] = cost
                heapq.heappush(q, (cost, x, y))

while True:
    n = int(stdin.readline())
    if n == 0:
        break

    graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    dijkstra()
    cnt += 1