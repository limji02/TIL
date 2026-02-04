import sys

sys.stdin = open('4836.txt')

# 10*10 격자판에 각각 입력된 빨간색 영역과 파란색 영역 중 겹치는 칸 수를 구하라.

T = int(input())

for tc in range(1, T + 1):
    # 10*10 격자판을 만든다. 각 tc마다 초기화.
    arr = [[0] * 10 for _ in range(10)]

    N = int(input())

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())  # 받은 값을 한 번에 다중 변수 할당

        # 영역 색칠하기
        for r in range(r1, r2 + 1):  # r2 까지 포함하여 순회
            for c in range(c1, c2 + 1):  # c2 까지 포함하여 순회
                # 만약 받은 값의 color 변수가 1이라면,
                if color == 1:
                    arr[r][c] += 1  # 현재 위치(r, c)에 빨강(1) 추가
                # 만약 받은 값의 color 변수가 2라면,
                elif color == 2:
                    arr[r][c] += 2  # 현재 위치(r, c)에 파랑(2) 추가
    # 총합 초기화
    sum_c = 0
    for r in range(10):
        for c in range(10):
            # 만약 현재 위치가 보라(3)라면,
            if arr[r][c] == 3:
                # 보라 갯수 하나 추가
                sum_c += 1

    print(f'#{tc} {sum_c}')