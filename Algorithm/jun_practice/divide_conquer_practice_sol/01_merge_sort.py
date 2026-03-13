"""
병합 정렬 (Merge Sort)
- 배열을 끝까지 반으로 나눈(Divide) 뒤, 정렬하면서 다시 합치는(Merge) 과정을 재귀적으로 구현
"""


def merge(left_arr, right_arr):
    """
    이미 정렬된 두 배열(left_arr, right_arr)을
    하나의 정렬된 배열로 '병합'하는 함수
    """
    merged_arr = []
    left_idx, right_idx = 0, 0

    # 1. 두 배열을 비교하며 작은 값부터 merged_arr에 추가
    # 두 배열 중 하나라도 원소가 남아있는 동안 반복
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        # 왼쪽 배열의 값이 더 작거나 같으면, 결과에 추가하고 왼쪽 포인터 이동
        if left_arr[left_idx] <= right_arr[right_idx]:
            merged_arr.append(left_arr[left_idx])
            left_idx += 1
        # 오른쪽 배열의 값이 더 작으면, 결과에 추가하고 오른쪽 포인터 이동
        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1

    # 2. 한쪽 배열이 먼저 끝났을 경우, 남은 요소들을 그대로 이어 붙임
    # (한쪽 배열은 이미 모든 원소가 소진되었으므로, 둘 중 하나만 실행됨)
    merged_arr.extend(left_arr[left_idx:])
    merged_arr.extend(right_arr[right_idx:])

    return merged_arr


def merge_sort(arr):
    """
    병합 정렬을 재귀적으로 구현하는 '매니저' 함수
    """
    # [기저 조건] 배열 길이가 1 이하면 이미 정렬된 상태
    if len(arr) <= 1:
        return arr

    # [1단계: 분할] 절반으로 나누기
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # [2단계: 정복] 각각을 재귀적으로 정렬
    # left_half와 right_half는 결국 정렬된 상태로 반환됨
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # [3단계: 통합] 정렬된 두 배열을 병합
    return merge(left_sorted, right_sorted)


# --- 테스트 ---
data = [69, 10, 30, 2, 16, 8, 31, 22]
print(f"정렬 전: {data}")  # [69, 10, 30, 2, 16, 8, 31, 22]
print(f"정렬 후: {merge_sort(data)}")  # [2, 8, 10, 16, 22, 30, 31, 69]
