import sys
from collections import deque  # deque

sys.stdin = open('5097.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 1. append()와 pop()으로 풀어보기

    # for i in range(M):
    #     arr.append(arr.pop(0))
    # print(f'#{tc} {arr[0]}')

    # 2. deque로 풀어보기
    dq = deque(arr)
    dq.rotate(-M)
    print(f'#{tc} {dq[0]}')







