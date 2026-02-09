import sys
sys.stdin = open('prac_1.txt')

T = int(input())

for tc in range(1, T + 1):
    word = input()
    result = word[::-1]

    print(f'#{tc} {result}')

# # 다른 방법
#
# for test_case in range(1, T+1):
#
#     word = input()
#     reverse_word = "" # 뒤집은 문자를 담을 곳
#
#     for w in word:
#         # 가장 앞에 있는 문자를 먼저 가져오기 때문에
#         # 앞 쪽에 먼저 넣어준 후 이미 넣어놓은 문자들과 합해준다
#         reverse_word = w + reverse_word
#     print(reverse_word)