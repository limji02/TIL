import sys

sys.stdin = open('prac/5185.txt')

# 16진수 각 자리 수를 4자리 2진수로 표시
# 2진수의 앞자리 0도 반드시 출력

def hex_to_b(hex_str):

    b_results = ''
    for char in hex_str:
        de = int(char, 16)
        b_str = format(de, '04b')
        b_results += b_str


    return b_results

T = int(input())

for tc in range(1, T + 1):
    N, hex_str = input().split()
    results = hex_to_b(hex_str)

    print(f'#{tc} {results}')
