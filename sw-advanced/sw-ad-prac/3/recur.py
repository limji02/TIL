# 중복순열을 출력하는 코드

path = []

def recur(cnt):
    if cnt == 3:
        print(path)
        return
    
    for i in range(1, 7):

        path.append(i)
        recur(cnt + 1)
        path.pop()


recur(0)

# ---  #

path = []
N = 6
used = [0] * N

def recur2(cnt):
    if cnt == 3:
        print(*path)
        return
    for i in range(1, 7):
        path.append(i)
        recur2(cnt + 1)
        path.pop()

recur2(0)