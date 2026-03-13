# 베이비진 게임
# run과 triplet
# p1과 p2의 대결 !! 6장 채우기 전이라도 먼저 run or triplet 되면 승자
# 가져가는 순서대로 12장 카드 정보 ㅇ -> 승자 출력
# 무승부 시에는 0을 출력 (모두 가져갈 때까지 없다면)

# 카드 한 장씩 가져갈 때마다 확인하기? 
# 짝수 번째 인덱스 순서에서 확인이 된다면 p1의 승리


import sys

sys.stdin = open('5203.txt')

def is_run(used_cards):

    sorted_cards = sorted(list(set(used_cards)))
    if len(sorted_cards) < 3:
        return False
    
    # 연속된 3개의 숫자가 있는지 확인
    for i in range(len(sorted_cards) - 2):
        if sorted_cards[i] + 1 == sorted_cards[i + 1] and sorted_cards[i + 1] + 1 == sorted_cards[i + 2]:
            return True
    return False

def is_triplet(used_cards):
    # 각 숫자의 개수를 세어서 3개 이상인지 확인
    for c in used_cards:
        if used_cards.count(c) >= 3:
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    N = len(cards)

    # 쓴 카드 리스트 저장할 것
    p1_used_cards = []
    p2_used_cards = []
    result = 0  # 기본값 무승부

    for i in range(N):
        # 짝수 번째 인덱스는 p1
        if i % 2 == 0:
            p1_used_cards.append(cards[i])
            # 카드 뽑은 직후 바로 승리 확인
            if is_run(p1_used_cards) or is_triplet(p1_used_cards):
                result = 1
                break
        else:
            p2_used_cards.append(cards[i])
            # 카드 뽑은 직후 바로 승리 확인
            if is_run(p2_used_cards) or is_triplet(p2_used_cards):
                result = 2
                break
        

    print(f'#{tc} {result}')



### --- 그냥 아래처럼 0~9 숫자를 카운트할 배열을 만드는 방식이 나을 것 같네요 --- ###

# 승자 판별 함수
def check_babygin(counts):
    for i in range(10):
        # 1. Triplet 체크 (동일한 카드가 3장 이상)
        if counts[i] >= 3:
            return True
        # 2. Run 체크 (연속된 숫자가 각각 1장 이상)
        if i <= 7: # 인덱스 범위 주의
            if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
                return True
    return False

T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    
    # 0~9까지 숫자를 카운트할 배열
    p1_counts = [0] * 10
    p2_counts = [0] * 10
    result = 0 # 무승부 기본값

    for i in range(len(cards)):
        if i % 2 == 0: # 첫 번째, 세 번째... (Player 1)
            p1_counts[cards[i]] += 1
            if check_babygin(p1_counts):
                result = 1
                break
        else: # 두 번째, 네 번째... (Player 2)
            p2_counts[cards[i]] += 1
            if check_babygin(p2_counts):
                result = 2
                break

    print(f'#{tc} {result}')