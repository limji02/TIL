import sys

sys.stdin = open('prac/03.txt')

# 암호 비트 패턴
# 16진수 배열이 주어질 때, 왼쪽부터 순차적으로 암호 비트 패턴을 찾아 출력
# 문제에서 주어진 6비트 암호 비트패턴을 딕셔너리로 저장합니다.
code_map = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,
}

def hex_to_b(hex_str):
    # 16진수 문자열을 2진수 문자열로 변환
    b_str = ''
    for char in hex_str:
        b = int(char,16)
        b_str += format(b, '04b')

    # 슬라이딩 윈도우
    results = []
    idx = 0

    while idx <= len(b_str) - 6:
        chunk = b_str[idx : idx + 6]

        if chunk in code_map:
            results.append(code_map[chunk])
            idx += 6
        else:
            idx += 1

    return results

T = int(input())

for tc in range(1, T + 1):
    hex_str = input().strip()
    h_results = hex_to_b(hex_str)

    print(f'#{tc}', *h_results)