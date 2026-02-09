def selection_sort(arr):
    """
    선택 정렬 (Selection Sort):
    - 매 회차마다 '남은 구간'에서 최솟값을 '선택'하여 정해진 위치로 옮기는 방식
    """
    n = len(arr)
    # 1. [외부 반복]
    # 정렬할 위치(i)를 하나씩 결정해 나간다.
    # 마지막 원소 하나가 남았을 때는 이미 정렬된 상태이다.
    # 그렇기 때문에 n-1번만 반복하면 된다.

    for i in range(n-1):  # k번째로 작은 원소를 찾으려면? k번째까지만 반복하면 됨
        # 일단 현재 위치를 최솟값이라고 가정
        min_idx = i

        # 2. [내부 반복]
        # 아직 정렬되지 않은 나머지 부분을 탐색한다.
        # i 값은 0,1,2,3 가지만, j는 1,2,3,4 가야 한다. 그러므로 j는 i+1부터 끝까지(n) 탐색

        for j in range(i+1, len(arr)):
            # 현재 가정된 최솟값보다 더 작은 값을 발견하면?
            if arr[j] < arr[min_idx]:
                min_idx = j
                # 이거 다 돌면 최솟값 min_idx 찾을 수 있다.

        # 3. [교환]
        # 탐색이 끝난 후, 진짜 최솟값을 현재 자리로 가져옴
        # (만약에 min_idx와 i가 같자면 제자리 교환이 일어나므로, 로직상 문제는 없다.)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 큰 외부반복에서 i가 현재 자리이므로...


# --- 실행 및 검증 ---
numbers = [2, 5, 1, 3, 4]
print(f"정렬 전: {numbers}")

selection_sort(numbers)

print(f"정렬 후: {numbers}")
