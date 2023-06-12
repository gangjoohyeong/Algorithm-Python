# 주식 하나 사기
# 가지고 있는 주식 팔기 (원하는 만큼)
# 가만 있기
# 최대 이익 계산하는 프로그램
from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    cnt = 0
    day = int(stdin.readline())
    prices = list(map(int, stdin.readline().split()))

    while len(prices) > 1:
        max_price = max(prices)
        max_price_idx = prices.index(max_price)

        for price in prices[:max_price_idx]:
            cnt += (max_price - price)

        prices = prices[max_price_idx+1:]

    print(cnt)