import sys

sys.stdin = open('miro.txt')

# 델타 4방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def mazerunner(r, c):

    if maze[r][c] == 3:
        return 1

    visited[r][c] = True
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if (maze[nr][nc] == 0 or maze[nr][nc] == 3) and not visited[nr][nc]:
               if mazerunner(nr, nc) == 1:
                   return 1
                      
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start_r, start_c = r, c
                result = mazerunner(start_r, start_c)
                
    print(f'#{tc} {result}')

