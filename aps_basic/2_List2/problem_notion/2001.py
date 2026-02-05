import sys

sys.stdin = open('2001.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())       # N*N = 파리행열, M*M = 파리채
    arr = [list(map(int, input().split())) for _ in range(N)]   # 파리 수

    # 인접한 거 최댓값 구하기

    # 8방향 델타를 써서 풀거예요

    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    total_sum = 0
    total_list = []

    for r in range(N):
        for c in range(N):
            # 현재 위치 (r, c)에서 8방향 탐색 시작!
            for d in range(8):
                nr = r + dr[d]  # 다음 행 (next row)
                nc = c + dc[d]  # 다음 열 (next column)

                M

                # 배열의 범위를 벗어나지 않는지 체크!
                if 0 <= nr < N and 0 <= nc < N:
                    total_sum += arr[nr][nc]
            total_list.append(total_sum)

    print(total_list)









   #
   # print(f'#{tc} {}')
