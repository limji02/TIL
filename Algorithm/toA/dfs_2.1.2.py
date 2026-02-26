import sys

sys.stdin = open('dfs_2.1.2.txt')

def dfs_recursive_list(current_node, adj_list,  visited, path):
    visited[current_node] = True
    path.append(current_node)

    for next_node in adj_list[current_node]:
        if not visited[next_node]:
            dfs_recursive_list(next_node, adj_list, visited, path)

V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_list =[[] for _ in range(V + 1)]

for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

visited = [False] * (V + 1)
traversal_path = []

dfs_recursive_list(1, adj_list, visited, traversal_path)

print(''.join(map(str, traversal_path)))