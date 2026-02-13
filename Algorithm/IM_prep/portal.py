# # 포탈

# import sys

# sys.stdin = open('portal.txt')

# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     # 방의 번호가 1번부터 N번까지이기 때문에, 헷갈리지 않기 위해 인덱스 0번에 임시 0번 할당
#     P = [0] + list(map(int, input().split()))

#     # 방 번호와 인덱스 번호 맞추기

#     portal = 0  # 포탈 몇 번 썼는지 누적
#     zumping = []  # 현재 방에서 다음 방으로 가기 위해 몇 번의 점프가 필요한가

#     # 1번 방은 무조건 2번 방으로 바로 이동하는 예외 조건도 있어야 함

#     for i in range(1, N+1):
#         portal += i - P(i)


#     print(f'{tc} {portal}')

import sys
sys.stdin = open('portal.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room_lst = [0] + list(map(int, input().split()))
    visit_count = [0] * (N + 1) # 각 방을 몇 번 밟았는지 기록
    current = 1 # 출발 방은 1번                
    steps = 0  # 총 포탈 이용수                
    while current < N: # 도착하기 전까지 반복
        steps += 1  # 일단 한 걸음~
        if current == 1: # 1번 방이면 바로 2번
            current = 2
            continue
        visit_count[current] += 1 # 왔다는 신호를 기록함.(1로)
        if visit_count[current] == 1: # 안 왔으면?
            current = room_lst[current] # 방 리스트의 위치로 이동
        else: # 이미 왔었으면?
            current += 1 # 오른쪽으로 1칸 이동

    print(f'#{tc} {steps}')
