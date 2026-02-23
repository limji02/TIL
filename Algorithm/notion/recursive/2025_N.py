# 반복문 활용
def get_sum_all(N):
    sum_i = 0
    for i in range(1, N + 1):
        sum_i += i
    return sum_i

# 재귀
def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)

N = 10
print(recursive_sum(N))

# 한 줄
N = 10
# print(N * (N + 1) // 2)