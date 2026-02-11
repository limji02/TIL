import sys

sys.stdin = open('01.txt')


def infix_to_postfix(expression):
    # 피연산자는 바로 출력, 연산자는 스택에 push
    # 수식이 끝나면 스택에 남아있는 연산자를 모두 pop하여 출력

    # 연산자를 저장할 스택과 결과를 담을 리스트를 만들어야 한다.
    stack = []
    result = []

    # 하나씩 순회하며 처리
    for token in expression:
        # 1. 피연산자는 바로 결과에 추가
        if token.isdigit():
            result.append(token)

        # 2. 연산자는 일단 스택에 저장
        else:
            if token.strip():
                stack.append(token)

    # 3. 스택에 남은 연산자를 모두 pop하고 결과에 추가하기
    while stack:
        result.append(stack.pop())
    return ''.join(result)


# 입력 받고 결과 출력
T = int(input())

for tc in range(1, T + 1):
    expr = input()
    result = infix_to_postfix(expr)
    print(f'{tc} {result}')