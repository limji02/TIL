def counting_sort(input_arr, k):
    pass
    # 1단계
    # 숫자 카운팅(빈도수 계산)

    # 각 숫자 카운팅 리스트 초기화, k값이 들어가기 위해 k+1개 만큼 자리를 만들어야 한다.
    freq_arr = [0] * (k+1)
    # 각 숫자 카운팅하여 넣기
    for num in input_arr:
        freq_arr[num] += 1

    # 2단계
    # 누적 합 계산
    # 누적 합 arr가 arr의
    for i in range(1, k+1):
        freq_arr[i] += freq_arr[i-1]

    # 3단계
    # 오름차순 정렬

    # 오름차순 정렬 리스트 초기화
    # 렬된 결과를 담을 ascending_arr는 입력받은 배열의 길이(len(input_arr))와 같아야 한다.
    ascending_arr = [0] * len(input_arr)  # ascending_arr = [0] * (k+1) 이렇게 하는 것보다 왼쪽이 괜찮다.

    # num 역순 순회 및 최종 배치
    for num in input_arr:
        freq_arr[num] -= 1  # freq_arr(누적합된 리스트) 중 해당 num(인덱스 번호)의 값을 하나 감소
        ascending_arr[freq_arr[num]] = num  # 감소된 값으로 ascending_arr의 인덱스 위치를 찾아, num을 최종 배치

    return ascending_arr


arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]