# 신청서 N 장에는 각각 작업 시작 시간 s와 완료 시간 e가 표시
# 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.
# 0시부터 다음날 0시 이전까지 (24시간 내) 최대 몇 대의 화물차가 이용할 수 있나

# 어떤 화물을 먼저 선택해야 할까?
# 종료 시간! 종료 시간이 바를수록 뒤에 다른 작업을 할 수 있는 여유 시간이 더 많이 확보되기 때문이다.
# 
import sys

sys.stdin = open('5202.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    se_list = [list(map(int, input().split())) for _ in range(N)]

    # lamda 활용해서 종료 시간 기준으로 리스트 정렬
    # 기준을 종료 시간으로만 둔다면, 종료 시간이 같은 경우에는 애매해 질 수 있으므로... 
    # 같은 경우에는 시작 시간 기준으로 오름차순 정렬
    se_list.sort(key=lambda x: (x[1], x[0]))

    # 마지막 종료 타임  (업데이트될 예정
    last_end_time = 0

    # 화물차 이용 누적
    cnt = 0

    for s,e in se_list:
        # 시작 시간이 마지막 종료시간보다 같거나 클 경우...
        if s >= last_end_time:
            cnt += 1
            # 마지막 종료 시간 업데이트
            last_end_time = e

    print(f'#{tc} {cnt}')


## --- 가장 짧은 소요 시간 작업들부터 채워 넣는 방식 --- ## 
# 그러나, 이 방식은 반례가 존재할 수도 있다! -> 종료 시간이 빠른 순으로 정렬하는 것이 정석!
T = int(input())
for tc in range(1, T+1):
    # N: 신청서
    # schedule: [n][0] -> s: 작업 시작 시간, [n][1] -> e: 작업 종료 시간
    N = int(input())
    schedule = [list(map(int, input().split())) for _ in range(N)]

    time_table = [False]*24     # [0시 ~ 1시, 1시 ~ 2시, ... 23시 ~ 24시] 시간대 별 작업 할당 여부
    time_list = [[e-s, s, e] for s, e in schedule]
    time_list.sort()    # 작업 시간이 작은 순으로 정렬

    cnt = 0
    # 작업 시간이 적은 순부터 할당
    for time, s, e in time_list:
        if True not in time_table[s:e]:     # 해당 작업 시간대 안에 작업 할당된 것이 없으면,
            cnt += 1
            for i in range(s, e):   # 마지막 e는 안 넣어줘도 됨
                time_table[i] = True

    print(f"#{tc} {cnt}")