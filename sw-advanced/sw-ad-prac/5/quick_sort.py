import sys

sys.stdin = open('quick.txt')

# Lomuto

def partition(arr, start, end):
    
    # 1. 가장 끝 원소를 피벗으로 설정하기
    pv = arr[end]

    # i : pv 보다 작은 원소들이 모일 구역의 마지막 인덱스
    i = start - 1

    # pv 보다 작은 값 찾기
    # j : 현재 탐색 인덱스
    for j in range(start, end):
        if arr[j] < pv:
            # pv 보다 작은 값을 찾을 경우, i + 1
            i += 1
            # i 와 j의 위치가 다른 경우에만 교환하기
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
    # 마지막으로 pv(arr[end]) 
    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    return i + 1

def quick_sort(arr, start, end):
    # 배열 길이가 1 이하면 정렬된 상태 -> 분할이 더 이상 불가능
    if start < end:
        # 1. 분할
        pivot_idx = partition(arr, start, end)
        # 2. 정복 (재귀적)
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)

    

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, len(arr) - 1)
    results = " ".join(map(str, arr))
    
    print(f'#{tc} {results}')