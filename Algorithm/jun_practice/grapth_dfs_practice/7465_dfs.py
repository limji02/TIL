import sys

sys.stdin = open('7465.txt')

# dfs로 풀기
# 인접 리스트 생성해서 함수 돌면서 인접 애들 다 방문 처리하기

def dfs(node):

    visited[node] = True

    # 인접 리스트에 있는 애들 다 꺼내서 재귀
    for myf in adj_list[node]:
        if not visited[myf]:
            dfs(myf)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 인접 리스트 생성
    adj_list = [[] for _ in range(N+1)]
    visited = [False] * (N + 1)

    for _ in range(M):
        my, friend = map(int,input().split())
        adj_list[my].append(friend)
        adj_list[friend].append(my)

    # 무리의 개수
    group_cnt = 0

    for i in range(1, N + 1):
        # 여기 걸릴 때마다 그룹 카운트
        if not visited[i]:
            dfs(i)
            group_cnt += 1


    print(f'#{tc} {group_cnt}')

