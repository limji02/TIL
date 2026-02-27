import sys

sys.stdin = open('11351.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    Omok_pan = [list(input()) for _ in range(N)]

    result = 'NO'
    # 가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if Omok_pan[i][j] == 'o':
                cnt += 1
        if cnt >= 5:
            result = 'YES'

    # 세로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if Omok_pan[j][i] == 'o':
                cnt += 1
        if cnt >= 5:
            result = 'YES'
    
    # 대각선
    cnt = 0 
    for k in range(N):
        if Omok_pan[k][k] == 'o':
            cnt += 1
        elif Omok_pan[k][(N-1)-k] == 'o':
            cnt += 1
    if cnt >= 5:
        result = 'YES'

    print(f'#{tc} {result}')