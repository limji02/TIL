import sys
# from itertools import combinations

sys.stdin = open('4837.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))  # 부분 집합 원소의 수 # 부분 집합의 합

    # 1부터 12까지의 숫자를 원소로 가진 집합 A
    # 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하라
    # 해당하는 부분집합이 없는 경우 0을 출력

    # 1. 전체 집합 생성
    # 2. 모든 경우의 수 탐색
    # 3. 부분 집합 추출
    # 4. 조건 검사
    # 그 임시 리스트의 길이가 N? 그 임시 리스트의 합이 K?
    # 5. 카운트

    

    # # # conbinations 함수 사용
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # results = list(combinations(A, N))

    # cnt = 0
    # for i in results:
    #     if sum(i) == K:
    #         cnt += 1

    print(f'#{tc} {cnt}')