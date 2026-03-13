import sys

sys.stdin = open('4839.txt')

# l , r , c 
# c = int((l+r)/2)
# 이긴 사람이 누구인지 출력하기, 비긴 경우는 0을 출력
# c와 A가 같아지는 순간 바로 출력. 혹은 C와 B가 같아지면 바로 출력

# 누가 더 적은 횟수 만에 찾느냐 -> 재귀 돌 때마다 cnt 
# 재귀 ver.
def get_search_cnt(start, end, target, cnt):
    
    cnt += 1
    mid = (start + end) // 2
    
    if mid == target:
        return cnt
    
    # 탐색 범위 재설정 후 재귀 호출
    # 목표값이 중간값보다 작으면, 오른쪽 구역은 볼 필요 없음
    elif mid > target:
        return get_search_cnt(start, mid, target, cnt)
    # 목표값이 중간값보다 크면, 왼쪽 구역은 볼 필요 없음
    else:
        return get_search_cnt(mid, end, target, cnt)


T = int(input())
for tc in range(1, T + 1):
    # 전체 쪽수, A가 찾을 쪽 번호, B가 찾을 쪽 번호
    P, A, B = map(int, input().split())
    
    # 각각 몇 번만에 찾았는지 알아내기
    cnt_A = get_search_cnt(1, P, A, 0)
    cnt_B = get_search_cnt(1, P, B, 0)

    # 결과값에 따라 승자 저장
    winner = ""
    if cnt_A < cnt_B:
        winner = "A"
    elif cnt_B < cnt_A:
        winner = "B"
    else:
        winner = "0"

    print(f'#{tc} {winner}')