import sys
from collections import deque
sys.setrecursionlimit(100000)

N = int(input())
MAX = 6
cycle = False
link = [[] for _ in range(MAX)]
visited = [False] * MAX
isCycle = [False] * MAX
check = [-1] * N

# 순환선 판단
def dfs(cur, start, cnt):
    global cycle
    print("1 : ", cur, start, cnt)
    print("2 : ", cycle, visited)
    if cur == start and cnt >= 2:
        cycle = True
        print("탈 출")
        return
    visited[cur] = True
    print("3 : ", link)
    print("------------------------")
    for n in link[cur]: # 이어져있는 곳 하나씩 방문
        print("n : ", n)
        if not visited[n]: # 방문 체크
            print("first standard")
            dfs(n, start, cnt + 1)
        elif n == start and cnt >= 2:
            print("second standard")
            dfs(n, start, cnt)
def bfs():
    global check
    q = deque()
    
    for i in range(N):
        if isCycle[i]:
            check[i] = 0
            q.append(i)
            
    while len(q) != 0:
        cur = q.popleft()
        
        for n in link[cur]:
            if check[n] == -1:
                q.append(n)
                check[n] = check[cur] + 1
    for i in check:
        print(i, end = " ")
    return

for i in range(N):
    data = list(map(int, input().split()))
    link[data[0] - 1].append(data[1] - 1)
    link[data[1] - 1].append(data[0] - 1)
print(link)

for i in range(N):
    print("first : ", i)
    visited = [False] * N
    cycle = False
    dfs(i, i, 0)
    if cycle:
        isCycle[i] = True
        print("cycle : ", isCycle)


bfs()