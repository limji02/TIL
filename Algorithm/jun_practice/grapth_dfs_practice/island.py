import sys

sys.stdin = open('island.txt')

N, M = map(int, input().split())  # M 길이 문자열, N개의 줄
grid = [list(map(int, input())) for _ in range(N)]

# 8 방향 델타
# 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

island_cnt = 0
visited = [[False] * M for _ in range(N)]

# 상하좌우 대각선으로 연결된 하나 이상의 1으로 이루어진 섬...
# 걍 1 하나 있어도 섬이다. 카운트 해야 함.

for r in range(N):
    for c in range(M):
        if not visited[r][c] and grid[r][c] == 1:
            island_cnt += 1
            visited[r][c] = True
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True


print(island_cnt)

# 해당 문제 테스트 케이스에 한해서는 정답이 나오기는 하지만, 위 코드에는 문제가 있다.
# 섬의 일부를 발견했을 때, 바로 근처의 8칸만 확인하기 때문에, 'ㄱ'자 모양의 섬이나 길게 늘어진 모양의 섬이라면 방문 처리가 안 된다.
# 그래서 아래 코드와 같이 dfs를 사용하여 그 칸과 연결된 모든 땅을 재귀적으로 끝까지 찾아간다.


import sys

sys.stdin = open('island.txt')

N, M = map(int, input().split())  # M 길이 문자열, N개의 줄
grid = [list(map(int, input())) for _ in range(N)]

def dfs(r, c):
    visited[r][c] = True

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1 and not visited[nr][nc]:
            dfs(nr, nc)
            
# 8 방향 델타
# 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

island_cnt = 0
visited = [[False] * M for _ in range(N)]

for r in range(N):
    for c in range(M):
        if grid[r][c] == 1 and not visited[r][c]:
            island_cnt += 1
            dfs(r, c)

print(island_cnt)