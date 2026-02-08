import sys

sys.stdin = open('4828.txt')

# max와 min 값을 구해서 뺀다. 다양한 방법으로 시도!

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
	
    # # 1. bubble sort
    # for i in range(N-1, 0, -1):
    #     for j in range(i):
    #         if arr[j] > arr[j+1]:
    #            	arr[j], arr[j+1] = arr[j+1],arr[j]
                   
    # result = arr[N-1]-arr[0]

    # # 2. if
    # max_v = arr[0]
    # min_v = arr[0]

    # for i in range(N):
    #     if max_v == arr[i]:
    #         continue

    #     elif max_v < arr[i]:
    #         max_v = arr[i]
    #     elif min_v > arr[i]:
    #         min_v = arr[i]
    
    # result = max_v - min_v

    # 3. selection sort

    for i in range(N-1):
        min_idx = i
        for j in range(i+1,N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    result = arr[N-1] - arr[0]

    print(f'#{tc} {result}')