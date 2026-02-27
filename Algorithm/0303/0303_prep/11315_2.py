import sys

sys.stdin = open('11351.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    Omok_pan = [list(input()) for _ in range(N)]

    result = 'NO'

    print(f'#{tc} {result}')