# 0과 1로 이루어진 문자열 S
# 0의 개수: 짝수, 1의 개수: 짝수
# 문자 중 절반의 0, 절반의 1을 제거 -> 새로운 문자열 S_ 를 만든다
# 문자열 중 사전순으로 가장 빠른 것?

# 1은 앞에서부터 제거
# 0은 뒤에서부터 제거

from collections import Counter

s = list(input())
counter = Counter(s)

# 앞에서부터 1 제거
for _ in range(counter['1']//2):
    s.remove('1')

# 뒤에서부터 0 제거
s = s[::-1]
for _ in range(counter['0']//2):
    s.remove('0')

# 다시 원래 순서대로 만들어서 프린트
print("".join(s[::-1]))