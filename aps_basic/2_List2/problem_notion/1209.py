import sys

sys.stdin = open('1209.txt')

for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(0, 100)]

    # 전치 행렬을 만든다. (열의 합을 구하기 위해)
    trans_arr = list(map(list, zip(*arr)))

    # 행, 열, 대각선 각각의 합을 넣을 리스트 생성
    sum_list = []
    # 대각선 두 개 누적합 생성
    diag1_sum = 0
    diag2_sum = 0

    # 인덱스 하나로 순회하며 각각의 합 구하기
    for i in range(100):
        sum_list.append(sum(arr[i]))
        sum_list.append(sum(trans_arr[i]))

        diag1_sum += arr[i][i]  # 왼쪽 위에서 오른쪽 아래로 향하는 대각선은 행과 열의 인덱스가 같다.
        diag2_sum += arr[i][99 - i]  # 오른쪽 위에서 왼쪽 아래로 향하는 대각선은 행+열=N-1이다.

        sum_list.append(diag1_sum)
        sum_list.append(diag2_sum)

    print(f'#{tc} {max(sum_list)}')