def bubble_sort(arr):

    N = len(arr)

    # 외부 반복 for 문 : 정렬 범위를 뒤에서부터 하나씩 줄여나간다.
    for i in range(N-1, 0, -1):

        # 내부 반복 for 문 : 인접한 원소 비교하고 교환하기
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)