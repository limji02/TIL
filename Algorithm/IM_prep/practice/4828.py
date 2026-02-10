import sys

sys.stdin = open('4828.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # # 1. max - min
    # result = max(arr) - min(arr)

    # # 2. sorted
    # s_arr = sorted(arr)
    # result = s_arr[N-1] - s_arr[0]

    # # 3. selection sort
    #
    # for i in range(N-1):
    #     min_idx = i
    #     for j in range(i+1, N):
    #         if arr[j] < arr[min_idx]:
    #             min_idx = j
    #
    #     arr[i], arr[min_idx] = arr[min_idx], arr[i]
    #
    # result = arr[N-1] - arr[0]

    # # 4. bubble sort
    #
    # for i in range(N-1, 0, -1):
    #     for j in range(i):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    #
    # result = arr[N-1] - arr[0]

    # 5. Notion solution code
    max_v = arr[0]
    min_v = arr[0]

    for i in range(N):
        if i == 0:
            continue
        if arr[i] > max_v:
            max_v = arr[i]
        if arr[i] < min_v:
            min_v = arr[i]
    result = max_v - min_v

    print(f'#{tc} {result}')

    # 6.