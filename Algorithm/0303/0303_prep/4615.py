import sys

sys.stdin = open('4615.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    game = [list(map(int, input().split())) for _ in range(M)]

    # [r좌표, c좌표, 1or2(흑or백)]
    
    # 보드 판 만들기
    pan = [ [0] * (N+1) for _ in range(N+1) ]


    # 델타 탐색 저장해두기
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc = [1, 0, -1, 1, 1, 0, -1, -1]

    # 흑부터 시작
    # 돌을 놓을 수 있는 곳은 (1)빈 공간이며 (2)반대 색의 돌의 근처 상하좌우대각선에 자신의 색 돌이 있을 때 (3)그 색과 일직선인 곳
    # 그럼 그 사이에 있는 돌은 자신의 돌 색으로 바뀐다.
    # 번갈아가며 흑백 놓고, 돌 놓을 곳이 없다면 상대 색이 다시 돌 놓기
    # 빈 곳이 없거나 두 색 모두 놓을 곳이 없으면 게임 종료 후 보드에 있는 돌의 개수가 많은 플레이어 승

    # 아니 근데 이미 수는 다 둔 것이잖아?
    # 그러면 색 바뀌는 것만 저장 잘 하면 되겠네

    # 보드 판에 game 정보 순차적으로 저장
    # 하면서 동시에 실시간으로 사이에 낀 돌 색 바꿔주기

    # 우선 기본 돌 배치 판에 저장해두기
    m = N // 2
    pan[m][m] = 2
    pan[m+1][m+1] = 2
    pan[m][m+1] = 1
    pan[m+1][m] = 1

    # 게임 횟수 별 저장 값을 이용해 pan에 저장
    for i in range(M):
        gr = game[i][0]
        gc = game[i][1]
        color = game[i][2]

        # 빈 곳인지 확인하고 해당 1 or 2 값 저장
        if pan[gr][gc] == 0:
            pan[gr][gc] = color
            # 델타 탐색으로 상,하,좌,우,좌상,좌하,우상,우하 탐색
            for d in range(8):
                # 탐색한 곳 저장할 리스트 생성
                to_flip = []
                nr, nc = gr + dr[d], gc + dc[d]
                # 
                while True:
                    # 판 밖으로 나가지 않고
                    if nr < 1 or nr > N or nc < 1 or nc > N:
                        break
                    # 해당 탐색 부분이 빈 곳이라면
                    if pan[nr][nc] == 0:
                        break
                    # 
                    if pan[nr][nc] == color:
                        for fr, fc in to_flip:
                            pan[fr][fc] = color
                        break
                    else:
                        to_flip.append((nr,nc))
                        nr += dr[d]
                        nc += dc[d]
    black_cnt = 0
    white_cnt = 0
    
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if pan[r][c] == 1:
                black_cnt += 1
            elif pan[r][c] == 2:
                white_cnt += 1


    print(f'#{tc} {black_cnt} {white_cnt}')