import sys

sys.stdin = open('4873.txt')

T = int(input())

for tc in range(1, T + 1):
    string = input()

    stack = []

    for char in string:
        # 아무것도 없을 때 무조건 push
        if len(stack) == 0:
            stack.append(char)
        # 무언가 들어있으면 pop()해서 꺼내어 변수 할당
        elif len(stack) != 0:
            out_char = stack.pop()
            # 꺼낸 문자가 현재 문자랑 같지 않을 경우에는
            # 꺼낸 문자 다시 넣어주고, 현재 문자도 넣어주기
            if out_char != char:
                stack.append(out_char)
                stack.append(char)

            else:  # 같다면 넘어가기 (같은 문자 꺼낸 상태, 현재 문자도 리스트에 push하지 않는다.)
                continue

    print(f'#{tc} {len(stack)}')
