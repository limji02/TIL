import sys

sys.stdin = open('5185.txt')

# 내장함수 사용

T = int(input())
for tc in range(1, T + 1):
    N, hexadecimal = input().split()

    result = ''
    for char in hexadecimal:
        # 16 진수 -> 10 진수
        decimal_val = int(char, 16)

        # 10 진수 -> 2 진수
        binary_val_with_prefix = bin(decimal_val)

        # 접두사 0b 제거
        binary_val = binary_val_with_prefix[2:]

        # 문자열 길이가 4 되도록 왼쪽에 0 채우기
        four_bits = binary_val.zfill(4)

        # 변환된 4비트 문자열을 결과에 이어 붙이기
        result += four_bits

    print(f'#{tc} {result}')


# --- #


# 16진수 각 자리 수를 4자리 2진수로 표시
# 2진수의 앞자리 0도 반드시 출력

# def hex_to_b(hex_str):

#     b_results = ''
#     for char in hex_str:
#         de = int(char, 16)
#         b_str = format(de, '04b')
#         b_results += b_str


#     return b_results

# T = int(input())

# for tc in range(1, T + 1):
#     N, hex_str = input().split()
#     results = hex_to_b(hex_str)

#     print(f'#{tc} {results}')
