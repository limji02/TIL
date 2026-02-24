T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # for i in range(N):
    #     for j in range

    # 단조 증가 okay

    # 1. arr이 단조 증가를 하는가? -> 아니라면 -1 출력 (맞다면 이미 오름차순 정렬이 된 거 겠지?)
    # 2. 위 테스트 통과한 arr 받을 때, 10의 경우 -> 1, 0으로 분리
    # 3. 곱한 거 넣을 빈 리스트
    # 4. 분리한 숫자 가져와서 인덱스 번호 i < j 인 두 숫자끼리 곱한 값을 리스트에 저장
    # 5. 위 리스트 중 최댓값을 출력

    # 이게 아니었고요.,,

    for i in range(N):
        if arr[i] >= arr[i+1]:
        print(-1)

        else:
        arr 
        
       

    print(f'#{tc} {}')