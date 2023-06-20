# 14445
# 케이크(?) 자르기

n = int(input())
print( 0 if n == 1 else n // 2 if n % 2 == 0 else n // 2 + 1 )