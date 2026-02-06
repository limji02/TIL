def bubble_sort(arr):
    n = len(arr)

    # [외부 반복] 정렬 범위를 뒤에서부터 하나씩 줄여나갑니다.
    # range(n-1, 0, -1): n-1부터 1까지 역순으로 반복
    for i in range(n - 1, 0, -1):

        # [내부 반복] 0부터 i-1까지 인접한 원소를 비교합니다.
        # i 이후의 뒷부분은 이미 정렬이 완료된 상태이므로 비교할 필요가 없습니다.
        for j in range(i):

            # [비교 및 교환] 앞의 원소가 뒤의 원소보다 크다면?
            # 작다면? 아래 부등호만 반대로 하기
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap

    return arr

# 테스트
numbers = [64, 13, 9, 62, 3] # 요소 다섯 개인 리스트를 정렬
print(f"정렬 전: {numbers}")
print(f"정렬 후: {bubble_sort(numbers)}")

# 버블 정렬 위의 예시 손으로 써보기! 리스트 변화 등 추적까지...
# 버블 정렬을 배우는 이유

# 범위의 설정과 변화 : error index out of range...
# - 버블 정렬일 경우, 회차가 늘어날 수록 최대치의 범위가 계속 줄어든다.
# - 외부 반복과 내부 반복 (for 문) 외부 반복은 큰 범위를 나타내는 경우가 많다.
