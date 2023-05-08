from sys import stdin
n, x = map(int, stdin.readline().split())
li = list(map(int, stdin.readline().split()))
value = sum(li[:x])
max_sum = value
cnt = 1
for i in range(n - x):
    value += li[i+x] - li[i]
    if value > max_sum:
        max_sum = value
        cnt = 1
    elif value == max_sum:
        cnt += 1
if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(cnt)