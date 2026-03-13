import sys
from itertools import permutations

sys.stdin = open('baby2.txt')
# Greedy
# 각 숫자가 몇 장씩인지 세어 cnt 배열에 저장
# triplet을 먼저 찾아 제거 후, 남은 카드로 run을 찾자!

T = int(input())

# 각 케이스 하나씩 탐색할 것!
for tc in range(1, T + 1):
    cards = list(map(int, input().strip()))

    # 배열 만들어서 각 숫자 장수 저장하기
    cnt = [0] * 10
    for card in cards:
        cnt[card] += 1

    # triplet과 run 되었는지 확인용 -> 2 되면 baby-gin
    baby_gin_sets = 0

    # 1. triplet을 먼저 찾아서 제거
    for i in range(10):
        while cnt[i] >= 3:
            cnt[i] -= 3
            baby_gin_sets += 1

    # 남은 카드로 run을 찾아서 제거
    for i in range(8):  # 8, 9, 10은 run은 될 수 없으므로 할 필요 음슴
        while cnt[i] >= 1 and cnt[i + 1] >= 1 and cnt[i + 2] >= 1:
            cnt[i] -= 1
            cnt[i + 1] -= 1
            cnt[i + 2] -= 1
            baby_gin_sets += 1

    if baby_gin_sets == 2:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')


