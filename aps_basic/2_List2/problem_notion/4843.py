import sys

sys.stdin = open('4843.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 선택 정렬

    # 인덱스 i 번이 짝수일 때, 남은 숫자 중 최댓값을 찾아 i 번째로 가져온다.
    for i in range(N - 1):
        if i % 2 == 0:
            max_idx = i  # 일단 max_idx를 현재 위치 i 로 설정
            for j in range(i + 1, N):
                if arr[j] > arr[max_idx]:  # 만약 위치 j의 값이 위치 max_idx 값보다 크다면,
                    max_idx = j  # max_idx는 j로 수정
            arr[i], arr[max_idx] = arr[max_idx], arr[i]  # 자리 바꾸기
        # 인덱스 i 번이 홀수일 때는, 남은 숫자 중 최솟값 찾아 i 번째로 가져온다.
        else:
            min_idx = i
            for j in range(i+1, N):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    result = arr[:10]
    print(f'#{tc}',*result)  # 10개만 잘라 출력 형식에 맞게
    # {*result} 이런 식으로는 안 되는 군요?
    # 문자열 join 메서드 활용
    # print(f'#{tc} {" ".join(map(str, result))}')

    # 위 코드를 더 짧게 할 수도 있다니 ! (아래는 위 코드에 대한 AI의 수정 제안이다.)

    for i in range(N - 1):
        target_idx = i  # 이름을 target_idx로 통일하면 편해요!

        if i % 2 == 0:  # 짝수 회차: 최댓값 찾기
            for j in range(i + 1, N):
                if arr[j] > arr[target_idx]:  # max_idx(target_idx)와 비교!
                    target_idx = j
        else:  # 홀수 회차: 최솟값 찾기
            for j in range(i + 1, N):
                if arr[j] < arr[target_idx]:  # 이번엔 작은 놈 찾기
                    target_idx = j

        # 찾은 놈이랑 현재 위치 교환
        arr[i], arr[target_idx] = arr[target_idx], arr[i]








