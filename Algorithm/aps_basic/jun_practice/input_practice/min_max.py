import sys

sys.stdin = open('06.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 최댓값과 최소값의 위치를 인덱스 0번으로 설정한다.
    max_v = arr[0]
    min_v = arr[0]

    # 인덱스 1번부터 N번까지 반복
    for i in range(1, N):
        # i 번째 값이 더 크다면, 최댓값 재할당
        if max_v < arr[i]:
            max_v = arr[i]
        # i 번째 값이 더 작다면, 최솟값 재할당
        elif min_v > arr[i]:
            min_v = arr[i]

    # print의 위치가 중요하군요... 한 칸 앞에 둬서 출력값이 #3 838110 만 나와서 당황했습니다.
    print(f'#{tc} {max_v - min_v}')
