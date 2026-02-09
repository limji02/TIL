# 포탈

import sys

sys.stdin = open('portal.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 방의 번호가 1번부터 N번까지이기 때문에, 헷갈리지 않기 위해 인덱스 0번에 임시 0번 할당
    arr = [0] + list(map(int, input().split()))

    bang_arr = [0] * N + 1

    potal = 0  # 포탈 몇 번 썼는지 누적

    for i range(1, N+1):
        arr[i] = num
        num



    print(f'{tc} {result}')