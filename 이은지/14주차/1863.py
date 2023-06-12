# 스카이라인 쉬운거
# stack -> 최고 높이 이전까지를 스택에 저장해놓고
# 최고 높이 이후의 값과 같은게 있으면 하나로 카운트 

# 스택 맨 위 값보다 크면 넣는다
# 스택 맨 위 값 (top)보다 새로운 값이 (new)작으면 넣지 않고 pop한다 -> (new)얘랑 (top)이 크거나 같으면 pop 한다 (작아지면 continue)
#   new 보다 큰 값이 pop 되었다 -> 카운트 증가 시킴
#   new 와 같은 값이 pop 되었다 -> 카운트 증가 시킴
# 이걸 반복하면 됨 
from sys import stdin
input = stdin.readline

n = int(input())
stack = [0]
answer = 0

for _ in range(n):
    _, h = map(int, input().split())
    if h > stack[-1]:
        stack.append(h)
        answer += 1
    else:
        while h < stack[-1]:
            stack.pop()
            if h > stack[-1]:
                stack.append(h)
                answer += 1

print(answer)