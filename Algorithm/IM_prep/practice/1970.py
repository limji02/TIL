import sys

sys.stdin = open('1970.txt')

# 쉬운 거스름돈
# 거스름돈 N이 주어지면, 최소 개수로 거슬러 주기 위해 각 종류의 돈이 몇 개씩 필요한지 출력

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    counts = []

    for i in range(8):
        n = N // money[i]
        counts.append(n)

        N = N % money[i]

    # print(f'#{tc}\n', *counts) 실패의 교훈 !!
    print(f'#{tc}')
    print(*counts)