# 5972
# 택배 배송

import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # 양방향
    graph[b].append((a, c)) # 양방향

INF = 1e9

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

visited = [False] * (n+1)
distance = [INF] * (n+1)

dijkstra(1) # 1번 노드에서

print(distance[n]) # n번 노드까지의 최단 거리