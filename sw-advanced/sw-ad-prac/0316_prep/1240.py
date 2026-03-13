import sys

sys.stdin = open('1240.txt')


# 단순 2진 암호코드
# 10의 배수이면 올바른 암호고 그렇지 않으면 틀린 암호...
# 0이 주변에 있는 게 좀 걸리는데...ㅇ ㅣ걸 어쩌지?
# 어디부터 시작이고 끝인지 어떻게 알지?
# 56 개수를 세면 되나?
# 잘못된 암호코드는 뭐지?
# 1을 발견하면 일단 쭉 저장?
# 걍 한 줄로 주면 될걸 왜 2차원 리스트에 준 거지??

# 뒤에는 무조건 1이니까 뒤에서부터 보면 됨!

# 일단 딕셔너리 만들어
code_dic = {

    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    scan_area = [list(map(int, input())) for _ in range(N)]

    # 일단 줄 하나 찾고
    # 그 줄에서 뒤에서부터 1을 찾고 그 위치부터 56글자 찾음 돼!!!!!!!! 유레카
    for i in range(N):
        for j in range(M):
            if scan_area[i][j] == 1:
                scan_row = scan_area[i]
    
    # 뒤에서부터 탐색해서 1찾으면 일단 오른쪽 날려
    for i in range(len(scan_row) -1, -1, -1):
        if scan_row[i] == 1:
            scan_row = scan_row[ :i + 1]
            break

    # 왼쪽도 날려
    scan_row = scan_row[-56:]

    decoded_numbers = []

    # 7글자 씩 끊어서 저장해야 돼
    for i in range(0, 56, 7):
        seven = scan_row[i : i + 7]
        seven = ''.join(map(str, seven))

        # 순서대로 리스트에 담아
        # 딕셔너리에서 맞는 거 꺼내와서
        decoded_numbers.append(code_dic[seven])
        
        # 홀수 자리 합하고 x 3 + 짝수 자리 합  <--  이게 10의 배수가 되어야 올바른 암호 판정

    # 일단 0으로...
    result = 0

    even_sum = 0
    odd_sum = 0

    for i in range(len(decoded_numbers)):
        if (i+1) % 2 == 0:
            even_sum += decoded_numbers[i]
        else:
            odd_sum += decoded_numbers[i]

    result = odd_sum * 3 + even_sum


    if result % 10 == 0:
        # 함정 주의 !! 출력값은 계산된 결과가 아니라 그냥 합이다.
        code_result = sum(decoded_numbers)
    else:
        code_result = 0



    print(f'#{tc} {code_result}')
