import sys

sys.stdin = open('06.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, list(input())))

    # 0이 10개 있는 리스트를 만든다.
    # 0부터 9까지의 인덱스 번호를 각 카드 넘버라고 생각한다.
    # 이곳에 카드 넘버가 몇 번 나왔는지 저장할 예정이다.
    card_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # 리스트의 카드를 순회하며 해당 카드 넘버와 같은 card_count 인덱스 위치에 숫자를 하나씩 올린다.
    for i in arr:
        card_count[i] += 1

        # 가장 많은 장수
        max_cards = max(card_count)
        # 가장 많은 장수를 가진 카드 넘버 0 초기화
        card_num = 0

        # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
        # 뒤에서 부터 확인하면 카드 장수 같을 때 카드 넘버 큰 거 출력할 수 있다.
        for i in range(9, -1, -1):
            # 카드 장수가 max_cards 와 같다면,
            if card_count[i] == max_cards:
                card_num = i  # card_num 에 재할당 - 끝끝
                break

    print(f'#{tc} {card_num} {max_cards}')
