"""
퀵 정렬 (Quick Sort - Lomuto 파티션)
- 맨 뒤의 원소를 피벗(반장)으로 삼고, 피벗보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 보내는 로무토 방식을 구현
"""


def partition(arr, start, end):
    """
    분할(Partition)을 담당하는 실무자 함수.
    - 가장 오른쪽 원소(arr[end])를 피벗으로 설정.
    - 피벗보다 작은 값들은 왼쪽으로, 큰 값들은 오른쪽으로 재배치.
    - 최종적으로 피벗이 있어야 할 올바른 위치의 인덱스를 반환.
    """

    # 1. 가장 오른쪽 원소를 피벗으로 설정
    pivot = arr[end]

    # i: 피벗보다 작은 값들이 모일 구역의 마지막 인덱스
    # i: swap 할 위치
    i = start - 1

    # 2. start부터 end-1 까지 순회하며 피벗보다 작은 값 찾기
    # j : 현재 탐색하고 있는 인덱스
    for j in range(start, end):
        # 현재 값(arr[j])이 피벗보다 작다면?
        if arr[j] < pivot:
            # 피벗보다 작은 값을 찾았으므로, i를 증가(swap 할 위치를 오른쪽으로 이동)
            i += 1
            # [선택사항] i와 j의 위치가 다르면, 교환 (같으면 교환하지 않음)
            if i != j:
                # i와 j의 위치를 교환하여, 작은 원소를 왼쪽으로 보냄
                # 피벗보다 작은 값을 i 위치로 스왑 / 경계(i)와 현재 원소(j)의 위치를 교환
                arr[i], arr[j] = arr[j], arr[i]

    # 3. 마지막으로 피벗(arr[end])을 작은 값 구역 바로 다음(i+1)과 스왑
    # 모든 순회가 끝나면, i+1 위치가 피벗이 들어갈 자리
    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    # 피벗이 위치하게 된 최종 인덱스 반환
    return i + 1


def quick_sort(arr, start, end):
    """
    퀵 정렬을 재귀적으로 지시하는 '매니저' 함수.
    """
    # 기저 조건: 배열 길이가 1 이하(start >= end)면 이미 정렬된 상태
    # 즉, 분할이 더 이상 불가능한 상태 (최소 단위)
    if start < end:
        # 1. 분할: partition 함수를 사용해 피벗의 올바른 위치를 찾음
        pivot_idx = partition(arr, start, end)

        # 2. 정복: 피벗을 제외한 왼쪽, 오른쪽 구간을 재귀적으로 정렬
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)


# --- 테스트 ---
data = [3, 2, 4, 6, 9, 1, 8, 7, 5]
print(f"정렬 전: {data}")  # [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(data, 0, len(data) - 1)
print(f"정렬 후: {data}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
