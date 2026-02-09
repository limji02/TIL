import sys

sys.stdin = open('1966.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 버블 정렬 풀이
    # 인접한 두 원소를 비교하여, 위치를 맞교환, 뒤에서부터 정렬된다.
    # i 가 N-1일 때, j는 0부터 N-2 까지 움직이며 arr[j]와 arr[j+1]을 비교한 뒤, 자리를 바꾼다.

    # 외부 반복
    for i in range(N-1, 0, -1):  # 정렬 범위 n-1부터 1까지 역순 반복
        # 내부 반복
        for j in range(i):  # 0 부터 i-1까지 인접 원소끼리 비교 ( i 이후는 이미 정렬 완)
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]



    print(f'#{tc} {arr}')


    # 선택 정렬 풀이
    # 매 회차마다 남은 구간에서 최솟값을 선택하여 정해진 위치로 옮기는 방식이다.
    # i가 0부터 시작, j는 1부터 시작
    # i가 N-1일 때 j는 N, 즉, 이미 마지막 값과 비교하여 위치 선정하므로 i가 살펴볼 범위는 N이 아니라 N-1
    # 외부 반복
    for i in range(N-1):
        min_idx = i  # 현재 위치 최솟값 위치로 가정
        # 내부 반복
        for j in range(i+1, N):  # 정렬 전인 i-1~N 탐색
            if arr[j] < arr[min_idx]:
                min_idx = j  # 비교하여 최솟값 위치 갱신

        # j 탐색 끝난 후 최솟값을 현재 자리 i로 가져오기
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    print(f'#{tc} {arr}')
