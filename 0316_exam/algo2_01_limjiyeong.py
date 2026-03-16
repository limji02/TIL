# import sys
#
# sys.stdin = open('algo2_sample_in.txt')

# 무게 제한 내에서 최대 보물 가치를 가져갈거예요

# 재귀 함수를 만들 건데요
# 현재 방 번호, 현재 보물의 무게와 보물의 가치를 인자로 받아 업데이트해가며 갈 거예요
# 각 방에서는 보물을 갖고 왼쪽이나 오른쪽으로, 갖지 않고 왼쪽이나 오른쪽으로 4가지 선택이 가능하다.

def recur(current_room, current_w, current_v):
    # 최댓값
    global max_v

    # 제한 무게를 초과한 경우에는 빠이
    if current_w > K:
        return

    # 도착하면 종료, 현재 누적 가치가 최대 가치보다 높다면 갱신
    if current_v > max_v:
        max_v = current_v
        return

    # 재귀

    if left[current_room]:
        recur(left[current_room], current_w + info_sort[left[current_room] - 1][1],
              current_v + info_sort[left[current_room] - 1][2])
    if left[current_room]:
        recur(left[current_room], current_w, current_v)

    if left[current_room]:
        recur(right[current_room], current_w + info_sort[right[current_room]-1][1], current_v + info_sort[right[current_room]-1][2])
    if right[current_room]:
        recur(right[current_room], current_w, current_v)

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # 방의 개수 N, 배낭의 최대 무게 K
    # 방 번호 r, 보물의 무게 w, 보물의 가치 v, 직전 방 번호 p
    info = [list(map(int, input().split())) for _ in range(N)]
    # 방 번호마다 보물의 무게와 보물의 가치를 리스트로 저장

    info_sort = sorted(info)
    # print(info_sort)
    # 방 번호와 직전 방 번호를 이용해서 부모-자식 트리 저장할거예요.
    # 인접 리스트를 만들어야 하나

    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i in range(N):
        p, c = info[i][-1], info[i][0]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    # 총 가치 합 저장해둘 거 ㄱㄱ
    max_v = 0

    # # 리프 노드 저장
    # leaf_node = info[-1][0]

    # 루트 방부터 탐색
    recur(info[0][0], 0, 0)

    print(f'#{tc} {max_v}')