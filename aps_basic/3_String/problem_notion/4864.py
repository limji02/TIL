import sys

sys.stdin = open('4864.txt')

# str2에 str1과 일치하는 부분이 있으면 1출력, 아니면 0출력.

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()  # 여기서 일치하는 거 찾는 거임

    N = len(str1)
    M = len(str2)

    i = 0  # str1의 인덱스
    j = 0  # str2의 인덱스

    while i < N and j < M:  # 범위 안에서
        if str1[i] != str2[j]:
            # 불일치 -> 비교 시작 위치를 한 칸 앞으로
            j = j - i

            i = -1
        j += 1
        i += 1  # i = 0

    # 패턴의 끝까지 모두 일치해서 i가 N과 같아졌다면 (찾기 성공)
    if i == N:
        result = 1
    else:
        result = 0

    print(f'{tc} {result}')