# 10 진수를 2 진수로 변환
def demical_to_binary(n):
    binary_num = ""
    # 0보다 클 때까지 2로 나누면서 ((1.반복을 끝내는 조건 먼저 생각하고...))
    # 나머지를 정답에 추가  ((2.추가 구현하기))

    while n > 0:
        # 2. 2로 나눈 나머지를 구해서
        remain = n % 2
        # 3. 정답에 추가
        binary_num = str(remain) + binary_num
        # 1. 2로 나눈다
        n = n // 2

    return binary_num