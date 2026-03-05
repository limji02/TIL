import sys

sys.stdin = open('input.txt')

def dfs_recursive(current_node, adj_list, visited, path):
    # 현재 노드 방문 처리
    visited[current_node] = True
    path.append(current_node)

    # 현재 노드와 연결된 인접 노드들 순회
    for next_node in adj_list[current_node]:
        if not visited[next_node]:
            dfs_recursive(next_node, adj_list, visited, path)



V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_list = [[] for _ in range(V + 1)]

for i in range(E):
    n1, n2 = data[2 * i], data[2 * i + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

visited = [False] * (V + 1)
path = []

dfs_recursive(1, adj_list, visited, path)
print(''.join(map(str, path)))