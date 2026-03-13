import sys
from collections import deque

sys.stdin = open('5174.txt')

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    V = E + 1
    edge_info = list(map(int, input().split()))
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    for i in range(E):
        p, c = edge_info[i * 2], edge_info[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    q = deque([N])
    cnt = 0

    while q:
        current_node = q.popleft()
        cnt += 1

        if left[current_node] != 0:
            q.append(left[current_node])
        if right[current_node] != 0:
            q.append(right[current_node])

    print(f'#{tc} {cnt}')