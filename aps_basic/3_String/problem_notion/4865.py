import sys

sys.stdin = open('4865.txt')

T = int(input())

for tc in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())

    # 빈 딕셔너리 생성 {글자 : 개수}
    # 문자열 1의 글자 키로 넣기 개수는 일단 0
    # 반복문 사용하여 문자열 1의 키가
    # 문자열 2에 몇 개씩 있는지 세어서 해당 키의 값에 넣기
    # 값 모두 출력
    # 그 값에서 가장 큰 숫자 출력

    word_dict = {}

    for w in str1:
        word_dict[w] = 0

    for char in str2:
        if char in word_dict:
            word_dict[char] += 1

    result = max(word_dict.values())

    print(f'#{tc} {result}')