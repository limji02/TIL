import sys

sys.stdin = open('4831.txt')

# K 한번 충전으로 최대 이동 정류장 수, N 번은 종점, M개 정류장에 충전기 설치
# arr은 충전기 설치된 정류장 번호
# 조건 : 만약 종점에 도착할 수 없는 경우 0 출력
# 출발지에 충전기 있으나, 충전횟수에는 포함 안 됨 = 풀충전으로 시작
# 최소 충전횟수로 종점 도착하기 -> 충전수를 카운트 하기
# if문으로 종점에 도착할 수 없는 경우 0 출력해야 함
# 현재 위치를 팔로업해야하고 충전할 때마다 +K 정류장 수 만큼 위치 이동해야 함
# 그런데 그 위치에 충전소가 없다면? 다시 한 칸씩 뒤로 가야함..
# 그러다 내 자리로 다시 돌아온 경우 0 출력하고 끝
# for문 돌 때마다 1정거장씩 이동??
# N+1 크기 리스트 만들고 충전소 있는 곳만 1로 표시

# 테스트 개수 입력받기
T = int(input())

# 각 줄 마다 데이터 읽어와서 테스트 케이스 번호와 함께 답 출력하기
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 현재 위치 초기화
    current = 0
    # 충전횟수 초기화
    charge = 0
    # 마지막 충전 위치 초기화
    last_charge = 0

    charger_location = [0] * (N+1)
    for i in arr:
        charger_location[i] = 1

    # 현재 위치가 종점보다 작을 때까지...
    while current < N:
        # K 만큼 앞으로 가기
        current += K
        # K 만큼 앞으로 갔는데 현재 위치가 종점과 같거나 크면 바로 끝
        if current >= N:
            break

        # 만약 현재 위치에 충전소가 없다면?
        if charger_location[current] == 0:
            # 뒤로 한 칸씩 가기. 현재 위치 1일때까지 하기 반복. 위치 1되면 종료.
            while current > last_charge and charger_location[current] == 0:
                current -= 1
                # 했는데? 아까 전 위치로 돌아왔다하면 반복문 종료. charge = 0.
            if current == last_charge:
                charge = 0
                break


        # 만약 현재 위치가 1이라면
        # 2번째 시도. else: 도 삭제. 후진해서 찾은 충전소에서 기름을 안 넣고 그냥 출발하게 됨.
        # 1번째 시도. if charger_location[current] == 1:하면 종점 위치에 충전소가 있을 때 if문 실행되어 원하는 결과가 안 나옴.
            # 충전 횟수 +1, 마지막 충전 위치 업데이트
        charge += 1
        last_charge = current
            # 또, 앞으로 K 만큼 가기부터 시작

    print(f'#{tc} {charge}')