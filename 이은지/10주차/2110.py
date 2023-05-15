# 공유기 설치 https://www.acmicpc.net/problem/2110
from sys import stdin

n, c = map(int, stdin.readline().split())       # n: 집 개수, c: 공유기 개수
x = [int(stdin.readline()) for _ in range(n)]   # 집의 좌표 
x.sort()

# k = 1 부터 하나씩 늘리는 것보다 이분 탐색이 효율적
start = 1                       # 최소 거리
end = (x[-1] - x[0])            # 최대 거리
mid = (end + start) // 2        # 최소 거리 = mid 로 가정
answer = 0

if n == c:
    answer = min(a - b for a, b in zip(x[1:], x))
elif c == 2:
    answer = end
else:
    while start < end:              # start == end -> break
        now = x[0]                  # 공유기 시작 위치 
        idx = 0                     # 인덱스 초기화 
        print(f'==== mid = {mid} ====')
        for i in range(c-1):        # 첫번째 공유기는 x[0] -> c-1 번만 반복 
            # 다음 인덱스 지정 
            idx = next((i + idx for i, v in enumerate(x[idx:]) if v >= now + mid), -1) # 시간초과 예상 
            print
            if idx == -1:           # 더 이상 조건을 만족하는 x가 없음 (x에 없음)
                print('해당 조건을 만족하는 x가 없음')
                break
            now = x[idx]            # 다음 위치 업데이트 
            print(f'값: {now}, 인덱스: {idx}')
        # mid 가 너무 큰 경우 -> 왼쪽에서 탐색 
        if (idx == -1):
            print('mid 가 너무 큼 ')
            start = start
            end = mid               # start + end // 2 는 항상 mid 보다 작음 
            mid = (end + start) // 2
            continue
        # mid 가 너무 작은 경우 -> 오른쪽에서 탐색 
        elif idx <= n-1:
            print('mid 가 너무 작음 ')
            answer = mid            # 답 가능성 있음 -> 저장 
            start = mid + 1         # 최소 거리는 mid + 1 로 할당 
            end = end
            mid = (end + start) // 2

print(answer)
