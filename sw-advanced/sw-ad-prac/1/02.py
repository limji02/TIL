import sys

sys.stdin = open('prac/02.txt')
# 16진수 문자로 이루어진 배열을 2진수로 바꾸고
# 7비트씩 묶어 10진수로 변환하기

def hex_to_dec(hex_str):
    
    # 16진수 배열을 한 글자씩 가져와서 2진수로 바꾸고 2진수 문자열에 저장하기
    b_str = ''
    for char in hex_str:
        decimal_v = int(char, 16)
        # format(숫자, '04b') -> 10진수 정수를 4자리 2진수 문자열로... 남는 공간은 0으로 채우기
        b_str += format(decimal_v, '04b')

    
    # 7비트씩 잘라 10진수 변환
    results = []
    idx = 0
    # 특별 규칙! 만약 자른 7비트가 '0000000' 이면, 앞 4비트는 버리고 뒤에 3비트만 다음 chunk와 합쳐 진행한다.
    leftover_bits = ''
    
    while idx < len(b_str):
        needed = 7 - len(leftover_bits)
        chunk = leftover_bits + b_str[idx : idx + needed]
        idx += needed
        leftover_bits = ""

        if len(chunk) < 7 and idx >= len(b_str):
            if chunk:
                results.append(int(chunk, 2))
            break

        if chunk == '0000000':
            leftover_bits = chunk[4:]

        else:
            results.append(int(chunk, 2))
            
    return results

T = int(input())

for tc in range(1, T + 1):
    hex_str = input().strip()
    ans_list = hex_to_dec(hex_str)
    print(f'#{tc}', *ans_list)
