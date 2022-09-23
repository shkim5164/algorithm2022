from collections import deque
import sys

N = int(input())
targets = deque([int(input()) for _ in range(N)])
range_nums = deque([i + 1 for i in range(N)])
stack = list()
answer = list()
target_num = targets[0]
answer_stack = list()
while targets:
    if stack and target_num == stack[-1]:
        stack.pop()
        answer.append('-')
        targets.popleft()
        answer_stack.append(target_num)
        if targets :
            target_num = targets[0]
    else:
        if len(range_nums) == 0:
            break
        stack.append(range_nums.popleft())
        answer.append('+')

if len(answer_stack) == N:
    for i in answer:
        print(i)
else:
    print('NO')
    
# 5분 남김