from sys import stdin 
import heapq
# https://www.acmicpc.net/problem/5972
# 다익스트라 공부 필요
                
n, m = map(int, stdin.readline().split())   # n: node, m: edge
graph = [[] for _ in range(n+1)]            # index: node 번호 
distance = [int(1e9)] * (n+1)               # distance: 거리 저장 

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    # 양방향 연결 
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))          # q에 (우선순위, 값) 을 push
    distance[start] = 0                     # 시작 노드 초기화 

    while q:                                # q가 비어있을 때까지 반복
        dist, now = heapq.heappop(q)        # 우선순위가 가장 작은 값 (가장 작은 거리) pop

        if distance[now] < dist:            # 지금 노드의 거리가 최단거리보다 작다면 이미 방문함
            continue                        # 방문할 필요 X

        for i in graph[now]:                # 연결된 모든 노드 탐색
            cost = dist + i[1]              # cost 는 
            if cost < distance[i[0]]:       
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

print(distance[-1])