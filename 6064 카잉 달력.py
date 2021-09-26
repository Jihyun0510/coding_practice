
def check(m, n, x, y):
    while x <= m*n:
        if x%n == y%n:
            return x
        x += m
    return -1

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(check(m, n ,x, y))