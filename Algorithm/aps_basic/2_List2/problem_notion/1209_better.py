import sys

sys.stdin = open('1209.txt')

for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 1. 최댓값을 담을 변수 하나만 준비 (리스트 대신)
    max_result = 0

    diag1_sum = 0
    diag2_sum = 0

    for i in range(100):
        # 2. 행의 합, 열의 합을 구함과 동시에 최댓값 갱신
        row_sum = sum(arr[i])
        # 열의 합은 전치행렬을 만들지 않고 직접 인덱스로 접근하면 메모리가 절약됨
        # 만약 전치행렬을 쓴다면 sum(trans_arr[i])도 OK
        col_sum = sum(arr[j][i] for j in range(100))

        max_result = max(max_result, row_sum, col_sum)

        # 3. 대각선 누적
        diag1_sum += arr[i][i]
        diag2_sum += arr[i][99 - i]

    # 4. 루프가 "다 끝난 후" 대각선 합을 최종 비교
    max_result = max(max_result, diag1_sum, diag2_sum)

    print(f'#{tc} {max_result}')