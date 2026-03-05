import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(node):

    queue = deque()
    path = []
    visited[node] = True
    queue.append(node)

    while queue:
        curr = queue.popleft()
        path.append(curr)

        for nn in adj_list[curr]:
            if not visited[nn]:
                visited[nn] = True
                queue.append(nn)
    return path

V, E = map(int, input().split())
data = list(map(int, input().split()))
adj_list = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)

for i in range(E):
    n1, n2 = data[2 * i], data[2 * i + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

print(bfs(1))
