import sys

sys.stdin = open('4874.txt')

# 숫자는 스택에 넣는다
# 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다
# . 은 스택에서 숫자를 꺼내 출력

def forth(expression):

    stack = []

    for token in expression.split():
        # 숫자는 스택에 넣는다.
        if token.isdigit():
            stack.append(int(token))
        # '.'은 스택에서 숫자를 꺼내 결과에 넣는다.
        elif token == '.':
            if len(stack) == 1:  # 딱 하나만 남아야 성공 (마침표는 항상 마지막에 있으니)
                return stack.pop()
            else:
                return 'error'

        # 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
        else:
            if len(stack) >= 2:
                a = stack.pop()  # a가 나중에 들어온 애니까... 연산 순서 생각
                b = stack.pop()
                if token == '+': stack.append(b + a)
                elif token == '-': stack.append(b - a)
                elif token == '*': stack.append(b * a)
                elif token == '/': stack.append(b / a)
                else:
                    return 'error'
            else:
                return 'error'



# 입력 받고 출력
T = int(input())

for tc in range(1, T + 1):
    expr = input()

    print(f'{tc} {forth(expr)}')