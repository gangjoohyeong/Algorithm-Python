# 21736
# 헌내기는 친구가 필요해

from collections import deque

n, m = map(int, input().split())
array = [ list(input()) for i in range(n) ]
visited = [ [False] * m for i in range(n) ]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for i in range(n):
    for j in range(m):
        if array[i][j] == 'I':
            visited[i][j] == True
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and array[nx][ny] != 'X' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        if array[nx][ny] == 'P':
                            answer += 1
            break
print( answer if answer else 'TT' )