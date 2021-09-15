import sys

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0
            else:
                graph[a][b] = min(graph[a][k]+graph[k][b], graph[a][b])

answer = [sum(graph[x][1:n+1]) for x in range(n+1)]
print(answer.index(min(answer)))
