import sys

sys.stdin = open('4861.txt')

# 함수 만들어서 써보기!
def is_palindrome(word):
    word_len = len(word)
    for i in range(word_len//2):
        if word[i] != word[word_len - 1 - i]:
            return False
    return True

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))  # N*N 글자판  # M 길이의 회문
    arr = [list(map(str, input())) for _ in range(N)]
    result = ''

    # 가로 먼저 탐색
    for r in range(N):
        for c in range(N - M + 1):  # 각 단어 길이가 다르므로 범위 제한
            # 행 r의 열 c부터 M개 추출
            sub_word = arr[r][c : c + M]
            if is_palindrome(sub_word):
                result = "".join(sub_word)
                break
        if result: break  # 바깥쪽 for문이 불필요하게 도는 것을 방지

    # 세로 탐색 (가로에서 못 찾았을 경우)
    if not result:  # result 변수에 빈 문자열만 있다면 파이썬에서 False로 취급되기 때문에 세로 탐색 시작
        for c in range(N):
            for r in range(N - M + 1):
                # 열 c의 행 r부터 M개 추출
                c_word = []
                for i in range(M):
                    c_word.append(arr[r + i][c])

                if is_palindrome(c_word):
                    result = "".join(c_word)
                    break
            if result: break

    print(f'#{tc} {result}')


