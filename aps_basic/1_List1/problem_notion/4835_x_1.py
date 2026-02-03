import sys

sys.stdin = open('4835.txt')

# N개의 정수가 들어 있는 배열에서 이웃한 M개의 숫자의 합이 가장 큰 경우와 가장 작은 경우를 구하여 뺀 값을 구해야 한다.

# 테스트 개수 입력받기
T = int(input())

# 각 줄 마다 데이터 읽어와서 테스트 케이스 번호와 함께 답 출력하기
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # print(f'{tc} {result}')

# 첫 시도 기록
    #  i 를 시작점이 아니라 중심점으로 보아서, 만약 M이 짝수일 경우 어려움이 있다.
# 이웃한 M개의 수 나타내기 : 인덱스 값으로 표현, 중앙 값 i, 양 옆 각각 i-1, i+1
# 첫번째 T만 생각해본다면... i + (i-1) + (i+1)한 모든 값을 구하여 그 중 최댓값과 최솟값 찾아 빼기

    sum_all = []
# 양 옆 값은 M을 2로 나눈만큼 떨어져 있다.
    Nanu = M // 2
    for i in range(0, N+1):  # 리스트의 범위를 넘어설 위험이 크다. N=10, M=3인데, i = 9까지 돌면, arr[9:12]를 찾으려다 빈리스트를 더 하거나 오류 날 가능성
    # 양 옆 값 ㄱㄱ
        left = i-Nanu
        right = i+Nanu+1

        sum_v = sum(arr[left:right])
    # sum_v = sum(arr[left:(i+1)]) + arr[i] + sum(arr[(i+1):right])

        sum_all.append(sum_v)
        if 0 in sum_all:
            sum_all.remove(0)
    print(max(sum_all) - min(sum_all))
