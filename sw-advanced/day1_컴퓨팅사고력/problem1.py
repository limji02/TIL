import sys

sys.stdin = open('pro1.txt')

def func(b_str):
    # 전달 받은 7글자의 문자열을 뒤에서부터 탐색 -> 10진수로 변환하며 계산하기
    reversed_str = b_str[::-1]
    r = 0

    for j in range(len(b_str)):
       if reversed_str[j] == '1':
           r += 2 ** j 

    return r

word = input().strip()

# 입력받은 문자열 인덱스 기준으로 7글자씩 잘라서 함수에 전달
for i in range(0, len(word), 7):
    print(func(word[i:i+7]), end = ' ')
