import sys

sys.stdin = open('4834.txt')

# 숫자 카드 N장 (0~9)
# 가장 많은 카드에 적힌 숫자는?
# 그 숫자 카드의 장 수는?
# 위의 두 값을 출력하는 프로그램
# 카드 장수 같을 시, 숫자 큰 것 출력

from collections import defaultdict

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    card = list(map(int, input()))

    # 1. defaultdict 사용하여 쉽게 {카드 넘버:장 수} 구하기 
    # card_number = defaultdict(int)

    # for num in card:
    #     card_number[num] += 1

    # 2. defualtdict 없이 구하기

    card_number = {}

    for num in card:
        if num not in card_number:
            card_number[num] = 1
        else:
            card_number[num] += 1
    
    # 가장 많이 나온 카드 장 수 구하기 
    max_value = max(card_number.values())

    # 장 수가 같을 경우, 가장 높은 카드 넘버 숫자를 출력하기
    candidates = []

    for k, v in card_number.items():
        if v == max_value:
            candidates.append(k)

    # 위의 candidates 리스트 생성 코드를 컴프리헨션 사용하여 아래와 같이 한 줄로 표기할 수 있다.
    # candidates = [k for k, v in card_number.items() if v == max_value]

    max_key = max(candidates)

    print(f'#{tc} {max_key} {max_value}')