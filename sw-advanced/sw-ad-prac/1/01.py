import sys

sys.stdin = open('prac/01.txt')

binary_str = input().strip()

results = []

for i in range(0, len(binary_str), 7):
    chunk = binary_str[i : i + 7]

    # int(문자열, 2) --> 2진수로 표현된 문자열을 10진수 정수로 변경
    decimal_v = int(chunk, 2)

    results.append(decimal_v)

# 공백으로 구분하여 출력 가능!
print(*results)
