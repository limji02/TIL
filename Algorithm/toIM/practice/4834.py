import sys

sys.stdin = open('4834.txt')

# 0~9 숫자 카드 N장, 가장 많은 카드와 그 카드의 숫자를 출력
# 카드 장수가 같을 경우, 적힌 숫자가 큰 쪽 출력

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    # # 딕셔너리 활용하여 풀기
    #
    # card = {}
    #
    # for num in arr:
    #     if num in card:
    #         card[num] += 1
    #     else:
    #         card[num] = 1
    #
    # max_c = 0
    # results = []
    #
    # for v in card.values():
    #     if v > max_c:
    #         max_c = v
    #
    # for k, v in card.items():
    #     if v == max_c:
    #         results.append(k)
    #
    # result1 = max(results)
    # result2 = card[result1]

    # 리스트 만들어서 풀기

    # index = card number
    # value = how many cards?
    counts = [0] * 10

    for num in arr:
        counts[num] += 1

    max_num = 9  # 일단 9를 1등으로 가정
    for i in range(8, -1, -1):  # 거꾸로 도는 게 핵심! 8부터 0까지...
        if counts[i] > counts[max_num]:
            max_num = i

    result1 = max_num
    result2 = counts[max_num]

    print(f'#{tc} {result1} {result2}')