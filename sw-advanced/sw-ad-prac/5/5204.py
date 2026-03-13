import sys

sys.stdin = open('5204.txt')

# 교수 : 병합 정렬을 이용해 오름차순 정렬해
# L[0:N//2], Lp[N//2:N] -> 0부터 N//2까지, N//2부터 까지

# 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.

def merge_sort(arr):

    # 배열의 길이가 1 이하면 이미 정렬된 상태
    if len(arr) <= 1:
        return arr
    
    # 1.분할 - 반띵 ㄱㄱ
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]    
    
    # 2. 정복 - 재귀 정렬
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)


# 병합하는 함수 -> 여기서 cnt 하면 됨
def merge(left_arr, right_arr):

    global cnt

    # 핵심 !! 조건 추가 ~~~
    if left_arr[-1] > right_arr[-1]:
        cnt += 1

    merged_arr = []
    left_idx, right_idx = 0, 0

    # 1. 두 배열 비교하며 작은 값부터 merged_arr에 추가
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        # 왼쪽 배열 값 더 작거나 같으면, merged_arr에 추가. 왼쪽 포인터 이동
        if left_arr[left_idx] <= right_arr[right_idx]:
            merged_arr.append(left_arr[left_idx])
            left_idx += 1

        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1

    merged_arr.extend(left_arr[left_idx:])
    merged_arr.extend(right_arr[right_idx:])

    return merged_arr
    

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    cnt = 0
    sorted_nums = merge_sort(nums)

    # 출력 : N//2번째 원소 , 오른쪽 원소가 먼저 복사되는 경우의 수
    print(f'#{tc} {sorted_nums[N//2]} {cnt}')