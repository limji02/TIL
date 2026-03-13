import sys

sys.stdin = open('4831.txt')

# 전기버스 문제
# 어떻게 풀었더라...
# 전기버스 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있음
# 중간에 충전기가 설치되어 있는 M개의 정류장 번호가 주어짐
# 최소 충전으로 종점 도착 -> 몇 번 충전?
# 종점 도착 불가능한 경우 0을 출력
# 출발할 때는 완충 상태임

# greedy 
# 버스 이동을 추적해야 함 -> 리스트 일단 만들어야 할듯?
# 일단 출발, [K] 도착. 여기에 충전기가 있나? 없으면 한 칸씩 뒤로 가기
# 충전기 발견하면 거기서 또 +K 만큼 가기
# 위를 반복하면 되지 않을까?

T = int(input())  # 노선 수
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())  # 충전 시 최대 이동 가능 정류장 수 K, 종점 N, 충전기 설치된 정류장 개수 M
    bus_stop_num = list(map(int, input().split()))
    
    # 충전소 위치를 표시한 노선 생성
    stops = [0] * (N + 1)
    for i in bus_stop_num:
        stops[i] = 1

    now = 0
    charge_cnt = 0
    # 마지막으로 충전한 위치
    last_charge = 0

    while now + K < N:  # (현재 위치가 아닌) 다음 점프가 종점에 닿지 않는 동안 반복
        now += K 
        
        while stops[now] == 0:
            now -= 1

            if now == last_charge:
                charge_cnt = 0
                break
        
        # 안쪽 while문에서 break 걸렸는지 체크
        if charge_cnt == 0 and now == last_charge:
            break

        # 충전기 찾았다면 충전 횟수 증가 및 기준점 갱신
        charge_cnt += 1
        last_charge = now

    print(f'#{tc} {charge_cnt}')