import sys

sys.stdin = open('pro1.txt')

b_str = input().strip()

results = []

for i in range(0, len(b_str), 7):
    chunk = b_str[i : i + 7]
    decimal_value = int(chunk, 2)
    results.append(decimal_value)


print(*results)