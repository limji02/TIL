import sys

sys.stdin = open('1989.txt')

# 단어를 받아 회문이라면 1, 아니라면 0 출력

# T = int(input())
#
# for tc in range(1, T + 1):
#     word = input()
#     # 단어의 길이를 변수 N에 저장한다.
#     N = len(word)
#     M = N // 2
#     # reversed 단어 저장 변수
#     re_word = word[::-1]
#
#     # 단어의 길이가 홀수라면,
#     if N % 2 != 0:
#         if word[:M+1] == re_word[:M+1]:
#             result = 1
#         else:
#             result = 0
#     # 단어의 길이가 짝수라면,
#     else:
#         if word[:M+1] == re_word[:M+1]:
#             result = 1
#         else:
#             result = 0
#
#     print(f'#{tc} {result}')
#
#
# # 위의 코드를 AI에게...
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     word = input().strip()  # 공백 제거를 위해 strip() 추가 권장
#
#     # 원본과 뒤집은 결과가 같으면 1, 다르면 0
#     result = 1 if word == word[::-1] else 0
#
#     print(f'#{tc} {result}')
#
# # 위의 코드 리스트 컴프리헨션 없는 ver.
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     word = input().strip()
#
#     # 뒤집은 단어 생성
#     reversed_word = word[::-1]
#
#     # 비교 후 결과 할당
#     if word == reversed_word:
#         result = 1
#     else:
#         result = 0
#
#     print(f'#{tc} {result}')
#
#
# # reverse 기능 없이 인덱스 기능만으로 구현
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     word = input().strip()
#     N = len(word)
#
#     # 일단 회문이라고 가정 (1)
#     result = 1
#
#     # 단어의 절반(M)만큼만 반복하며 양 끝을 비교
#     for i in range(N // 2):
#         # i번째(앞)와 N-1-i번째(뒤) 글자가 다르면 회문이 아님
#         if word[i] != word[N - 1 - i]:
#             result = 0
#             break  # 하나라도 다르면 더 볼 필요 없이 종료
#
#     print(f'#{tc} {result}')


T = int(input())

for tc in range(1, T+1):
    word = input()
    N = len(word)

    result = 1  # 일단 해당 단어가 회문이라고 가정

    # 단어 길이의 절반만 보기
    for i in range(N // 2):
        # i번째(앞)와 N-1-i번째(뒤) 글자가 다르면 회문이 아니므로,
        if word[i] == word[N - 1 - i]:
            # 0으로 재할당
            result = 0
            break
    print(f'#{tc} {result}')
