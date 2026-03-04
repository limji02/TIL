# 2차원 배열 세로 읽기
# 스도쿠 문제에서도 활용할 수 있다.
# 목표
# 행 길이에 상관없이 세로로 순회하는 로직을 익히기 (문제 5356 의석이의 세로로 말해요 대비)

# 길이가 다른 문자열 5개
words = [
    "ABCDE",
    "abc",
    "012345",
    "SSAFY",
    "Python"
]

# [실습 1] 가장 긴 문자열의 길이(max_len)를 구하세요. 세로 순회의 최대 범위는 결국, 가장 긴 문자열의 길이이기 때문이다.
max_len = 0
# 반복문으로 최대 길이 갱신
for word in words:
    if  len(word) > max_len:
        max_len = len(word)

# max_len = max(len(word) for word in words)  # 최대 길이 갱신 -> 이렇게도 가능하다.

print(f"최대 길이: {max_len}")
result = ""

# -------------------------------------------------
# 세로 읽기 (Vertical Reading)
# -------------------------------------------------
# [실습 2] 세로로 읽기 위한 2중 반복문을 작성하세요.
# 2중 반복의 주체가 c, col(열)을 먼저 고정한 후에 row(행)을 순회해야 하기 때문이다.

for c in range(max_len):       # 열 인덱스 (0 ~ max_len-1)
    for r in range(len(words)): # 행 인덱스 (단어 개수)
        
        # [실습 3] 인덱스 에러 방지 (IndexError)
        # 현재 열(c)이 해당 단어(words[r])의 길이보다 작을 때만 읽어야 합니다.
        # 단어들의 길이가 다 다르기 때문이다.
        # 중간에 비는 곳은 그냥 넘어가게 하는 것이다.
        if c < len(words[r]):
            result += words[r][c]

print("세로 읽기 결과:", result)  # 세로 읽기의 결과를 result에 쌓아간다.
