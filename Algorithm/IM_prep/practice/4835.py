import sys

sys.stdin = open('4835.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    # 초기값 설정
    first_sum = 0
    for i in range(M):
        first_sum += arr[i]
    max_sum = first_sum
    min_sum = first_sum

    # 순회
    # 시작점 i를 순회하고 그 안에서 i~i+M를 누적한다.
    for i in range(N - M + 1):
        current_sum = 0
        for j in range(i, i + M):
            current_sum += arr[j]

        # 최대값 최솟값
        if max_sum < current_sum:
            max_sum = current_sum
        if min_sum > current_sum:
            min_sum = current_sum

    result = max_sum - min_sum
    print(f'#{tc} {result}')