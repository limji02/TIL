# 16811 당근 포장하기
#
import sys

sys.stdin = open('16811.txt')
T = int(input())

for tc in range(1, T + 1):
    N = int(input())    # N개의 당근
    arr = sorted(list(map(int, input().split())))

    # N 최대가 1000 이므로...
    result = 1001

    # 소, 중 나누는 기준점 i
    # 중, 대 나누는 기준점 j
    # 기준점 i와 j의 모든 경우의 수를 순회하며, 조건(크기 조건, 개수 조건)으로 필터링한다.
    for i in range(1, N-1):
        for j in range(i+1, N):
            # 경계선에 있는 당근들 크기 같으면 탈락(continue) (*인덱스로 빈 상자는 걸러짐)
            if arr[i-1] == arr[i] or arr[j-1] == arr[j]:
                continue
            s_arr = arr[:i]
            m_arr = arr[i:j]
            l_arr = arr[j:]

            s_count = len(s_arr)
            m_count = len(m_arr)
            l_count = len(l_arr)

            # 한 상자에 N//2 초과하면 탈락
            if max(s_count, m_count, l_count) <= N//2:
                # 두 조건 통과하면 diff 계산
                diff = max(s_count, m_count, l_count) - min(s_count, m_count, l_count)
                # 아래 if문이 반복되면 마지막에 최솟값이 저장된다.
                if diff < result:
                    result = diff

    # 단 한 번도 조건에 맞는 조합이 없어서 result가 그대로 1001이면?
    if result == 1001:
        result = -1


    # set_C_arr = list(set(C_arr))
    # j = (N//3)*2
    # s_arr = set_C_arr[:N//3]
    # m_arr = set_C_arr[N//3:j+1]
    # l_arr = set_C_arr[j:]

    print(f'#{tc} {result}')