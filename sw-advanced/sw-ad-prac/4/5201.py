# N : 컨테이너 개수
# M : N개의 컨테이너를 실은 트럭의 개수
# 트럭 1 : 컨테이너 1 씩
# 트럭의 적재용량 초과하는 컨테이너는 운반 불가능
# 최대 M대의 트럭이 편도로 한 번만 운행됨
# 이때 이동한 화물의 총 중량이 최대가 되도록, 옮겨진 화물 전체 무게 출력
# 싣지 못한 트럭 가능, 남는 화물 가능.
# 단 한 개의 컨테이너도 못 옮긴다면 0 출력


# 가장 큰 적재용량의 트럭에 가장 큰 화물부터 넣어야 이동한 화물의 총 중량이 최대가 됨
# 만약 가장 큰 적재용량의 트럭 < 가장 작은 화물이라면 0 출력

# 까지 생각하고 구현하는데...뭔가 안 됨! 

# 매 순간 가장 이득이 되는 선택(가장 무거운 화물을 가장 큰 트럭에)을 하기 때문에 greedy

import sys

sys.stdin = open('5201.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 무거운 순으로 정렬하기
    N_weights = sorted(list(map(int, input().split())), reverse=True)
    M_capacity = sorted(list(map(int, input().split())), reverse=True)

    total_w = 0
    w_idx = 0
    t_idx = 0

    while N_weights < N and M_capacity < M:
        # 현재 가장 무거운 화물이 현재 가장 큰 트럭에 들어가는지 확인
        if N_weights[w_idx] <= M_capacity[t_idx]:
            total_w += N_weights[w_idx]
            # 다음 화물과 다음 트럭에서부터 탐색
            t_idx += 1
            w_idx += 1
        else:
            # 해당 트럭에 들어가는 다음 화물 탐색
            w_idx += 1
        
    print(f'#{tc} {total_w}')
        

# w_sum = 0

#     # 트럭, 화물 삭제하면서 ㄱㄱ... 
#     for i in range(N):
#         for j in range(M):
#             if N_weights[i] <= M_capacity[j]:
#                 N_weights.pop(i)
#                 M_capacity.pop(i)
#                 result += N_weights[i]
#             if N_weights[-1] > M_capacity[0]:
#                 break