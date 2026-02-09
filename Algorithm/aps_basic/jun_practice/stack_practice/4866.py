import sys

sys.stdin = open('4866.txt')

T = int(input())

# if문으로 풀기
def check_brackets(string):
    stack = []

    # 반복문 : char 하나 씩 꺼내서 다음 if, elif, else문 체크
    for char in string:
        # 꺼낸 char이 여는 문자열에 있다면, stack에 추가하기
        if char in '([{':
            stack.append(char)
        # 꺼낸 char이 닫는 문자열에 있다면, 가장 최근에 추가했던 여는 괄호를 꺼내서 매칭 확인!
        elif char in '})]':
            open_char = stack.pop()

            if open_char == '(' and char != ')':
                return 0
            elif open_char == '[' and char != ']':
                return 0
            elif open_char == '{' and char != '}':
                return 0

        else:
            continue  # 괄호가 아니라면 넘어가기

    # 반복문이 모두 끝났는데 stack에 남아있는 게 없다면, 모든 괄호가 매칭이 된 것이다.
    if len(stack) == 0:
        return 1
    # stack에 무언가 남아있다면, 매칭되지 않은 괄호가 있다는 것이다.
    else:
        return 0

def check_brackets_dict(string):
    b_dict = {}

    for char in string:



# dict 으로 풀기
for tc in range(1, T + 1):
    line = input()
    print(f'#{tc} {check_brackets(line)}')
    print(f'#{tc} {check_brackets_dict(line)}')
