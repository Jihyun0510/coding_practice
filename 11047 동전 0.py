import sys

n, k = 10, 4200
# n, k = map(int, input().split())

coins = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
# for _ in range(n):
#     coins.append(sys.stdin.readline().rstrip())
answer = 0

for i in range(n-1, -1, -1):
    if coins[i] <= k:
        answer += k//coins[i]
        k = k%coins[i]

print(answer)