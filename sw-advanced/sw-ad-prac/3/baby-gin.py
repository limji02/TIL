import sys
from itertools import permutations

sys.stdin = open('baby.txt')
# 순열 활용 
# run 확인 함수
def is_run(cards):
    return cards[0] + 1 == cards[1] and cards[1] + 1 == cards[2]

# triplet 확인 함수
def is_triplet(cards):
    return cards[0] == cards[1] == cards[2]

N = int(input())
for tc in range(1, N + 1):
    cards = list(map(int, input()))
    is_babygin = False

    # 해당 숫자들의 모든 순열을 생성 후 중복 제거
    for p in set(permutations(cards)):
        # 앞 3장, 뒤 3장으로 그룹 나눔
        g1 = sorted(list(p[:3]))
        g2 = sorted(list(p[3:]))
        # 함수로 run과 tripelt 확인
        ch1 = is_run(g1) or is_triplet(g1)
        ch2 = is_run(g2) or is_triplet(g2)
        # 두 조건을 모두 만족하는 경우 찾아 저장하고 하나 찾으면 더 이상 탐색 필요 없음
        if ch1 and ch2:
            is_babygin = True
            break

    print(f'#{tc} {is_babygin}')