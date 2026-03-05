import sys
from collections import deque

sys.stdin = open('7465.txt')

def bfs(node):
    queue = deque([node])
    visited[node] = True

    while queue:
        curr = queue.popleft()

        for myf in adj_list[curr]:
            if not visited[myf]:
                visited[myf] = True
                queue.append(myf)

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    adj_list = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for _ in range(M):
        my, friend = map(int, input().split())
        adj_list[my].append(friend)
        adj_list[friend].append(my)

    group_cnt = 0

    for i in range(1, N + 1):
        if not visited[i]:
            bfs(i)
            group_cnt += 1

    print(f'#{tc} {group_cnt}')
        
