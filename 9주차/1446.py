n, d = map(int, input().split())
shortcuts = []
check_point = set([])

for _ in range(n):
    i = list(map(int, input().split()))
    if any(i > d for i in i[:2]):
        continue
    shortcuts.append(i)
    check_point.update(i[:2])
check_point.add(d)
check_point = sorted(list(check_point))

dp = {0:0}
for idx, cp in enumerate(check_point):
    prev_cp = list(dp.keys())[-1]
    dp[cp] = dp[prev_cp] + (cp - prev_cp)
    for shortcut in shortcuts:
        if shortcut[1] == cp:
            dp[cp] = min(dp[shortcut[0]]+shortcut[2], dp[cp])
print(dp[d])