# import sys
#
# sys.stdin = open('algo1_sample_in.txt')

# 모스 부호를 16진수로 변환하기

# 모스부호를 이진수로 변환하는 함수
def code_to_bin(code):
    for c in range(len(code)):
        if code[c] == '.':
            code[c] = '0'
        else:
            code[c] = '1'
    return "".join(code)

T = int(input())

for tc in range(1, T + 1):
    code = list(map(str, input().strip()))

    # 2진수로 변환한 함수 저장
    bin_str = code_to_bin(code)

    # 2진수로 변환한 것을 10진수로 먼저 변환
    int_str = int(bin_str, 2)

    # 10진수로 변환한 것을 16진수로 변환하고 앞에 자르고 대문자로 저장하기
    result = hex(int_str)[2:].upper()

    print(f'#{tc} {result}')
