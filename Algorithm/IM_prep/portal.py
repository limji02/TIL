# 포탈

import sys

sys.stdin = open('portal.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 방의 번호가 1번부터 N번까지이기 때문에, 헷갈리지 않기 위해 인덱스 0번에 임시 0번 할당
    P = [0] + list(map(int, input().split()))

    # 방 번호와 인덱스 번호 맞추기

    portal = 0  # 포탈 몇 번 썼는지 누적
    zumping = []  # 현재 방에서 다음 방으로 가기 위해 몇 번의 점프가 필요한가

    # 1번 방은 무조건 2번 방으로 바로 이동하는 예외 조건도 있어야 함

    for i in range(1, N+1):
        portal += i - P(i)

            

    print(f'{tc} {portal}')