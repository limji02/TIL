import sys

sys.stdin = open('01_Delta.txt')

T = int(input())

# 행렬 방향 상,하,좌,우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # N = len(arr) # 행의 길이
    # M = len(arr[0]) # 열의 길이

    # 총합
    total = 0

    for r in range(N):
        for c in range(N):
            sum_abs = 0  # 인근 값의 차 합계 (절대값)
            for idx in range(4):
                nr = r + dr[idx]
                nc = c + dc[idx]

                if 0 <= nr < N and 0 <= nc < N:  # 인덱스 범위 설정
                    new_num = arr[nr][nc]  # 대상 값을 저장
                    now_num = arr[r][c]  # 현재 값을 저장

                    sum_abs += abs(now_num - new_num)  # 대상 값과 현재 값의 차이를 절대값으로 저장

            total += sum_abs  # 총합 구하기

    print(f'#{tc} {total}')


