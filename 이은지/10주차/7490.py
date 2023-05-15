# 0 만들기 https://www.acmicpc.net/problem/7490
# 모든 경우의 수 고려? 공백 또는 + 또는 - (최대 경우의 수: 3**8)
from sys import stdin

k = int(stdin.readline())

def f(exp_list, i: int):
    result = []
    for exp in exp_list:
        result.append(exp + ' ' + str(i))
        result.append(exp + '+' + str(i))
        result.append(exp + '-' + str(i))
    return result

for _ in range(k):
    n = int(stdin.readline())
    exp_list = ['1']
    for i in range(2, n+1):
        exp_list = f(exp_list, i)
    
    for exp in exp_list:
        exp_ = exp.replace(' ', '') # eval() 적용을 위해
        if eval(exp_) == 0:
            print(exp)
    
    print('')