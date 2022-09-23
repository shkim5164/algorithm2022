import sys
from collections import deque

def setCommend(commend, queue):
    print_num = -1
    if commend == "pop":
        if len(queue) > 0:
            print_num = queue.popleft()
    elif commend == "size":
        print_num = len(queue)
    elif commend == "empty":
        if len(queue) == 0:
            print_num = 1
        else:
            print_num = 0
    elif commend == "front":
        if len(queue) > 0:
            print_num = queue[0]
    elif commend == "back":
        if len(queue) > 0:
            print_num = queue[-1]
    else:
        print_num = commend.split()[1]
        queue.append(print_num)
        return
    print(print_num)

# 첫번째 input
N = int(input())
cmds = [sys.stdin.readline().rstrip() for _ in range(N)]
queue1 = deque()
for cmd in cmds:
    setCommend(cmd, queue1)


# 24분 남김
