# 공유기 설치 https://www.acmicpc.net/problem/2110
from sys import stdin

n, c = map(int, stdin.readline().split())       # n: 집 개수, c: 공유기 개수
x = [int(stdin.readline()) for _ in range(n)]   # 집의 좌표 
x.sort()

# k = 1 부터 하나씩 늘리는 것보다 이분 탐색이 효율적
start = 1                       # 최소 거리
end = (x[-1] - x[0])            # 최대 거리
answer = 0

while start < end:
    now = x[0]                  # 공유기 시작 위치 
    idx = 0                     # 인덱스 초기화 
    mid = (end + start) // 2    # 최소 거리 = mid 로 가정

    for i in range(c-1):        # 첫번째 공유기는 x[0] -> c-1 번만 반복 
        # 다음 인덱스 지정 
        idx = next((idx + i for i, v in enumerate(x[idx:]) if v >= now + mid), -1) # 시간초과 예상 
        if idx == -1:           # 더 이상 조건을 만족하는 x가 없음 (x에 없음)
            break
        now = x[idx]            # 다음 위치 업데이트 
    
    # mid 가 너무 큰 경우 -> 왼쪽에서 탐색 
    if (idx == -1):
        start = start
        end = mid 
        continue
    # mid 가 너무 작은 경우 -> 오른쪽에서 탐색 
    elif idx <= n-1:
        result = mid            # 답 가능성 있음 -> 저장 
        start = mid + 1
        end = end

print(result)
