import sys

sys.stdin = open('dfs_2.1.1.txt')

def drm(current_node, adj_matrix, visited, path):

    visited[current_node] = True
    path.append(current_node)

    for next_node in range(1, len(adj_matrix)):
        if adj_matrix[current_node][next_node] and not visited[next_node]:
            drm(next_node, adj_matrix, visited, path)


V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

visited = [False] * (V + 1)
traversal_path = []

drm(1, adj_matrix, visited, traversal_path)

print(''.join(map(str, traversal_path)))