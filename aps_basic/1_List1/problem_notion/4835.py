import sys

sys.stdin = open('4835.txt')

# N개의 정수가 들어 있는 배열에서 이웃한 M개의 숫자의 합이 가장 큰 경우와 가장 작은 경우를 구하여 뺀 값을 구해야 한다.

# 테스트 개수 입력받기
T = int(input())

# 각 줄 마다 데이터 읽어와서 테스트 케이스 번호와 함께 답 출력하기
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 모든 경우의 합을 담을 리스트 생성
    sum_all = []

    for i in range(N - M + 1):  # 시작점 i가 가질 수 있는 마지막 값은 N - M + 1 이다.
        # i 부터 i + M까지 더한 값
        sum_v = sum(arr[i: i + M])
        # 을 리스트에 추가
        sum_all.append(sum_v)

    # 모든 경우의 합을 담은 리스트에 max와 min을 구해 빼기
    result = max(sum_all) - min(sum_all)
    print(f'#{tc} {result}')
