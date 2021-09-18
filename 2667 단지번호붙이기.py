from collections import deque, defaultdict

n = int(input())
# n = 7

graph = []
for _ in range(n):
    x = list(map(int, input()))
    graph.append(x)


# graph = [[0,1,1,0,1,0,0],[0,1,1,0,1,0,1],[1,1,1,0,1,0,1],[0,0,0,0,1,1,1],[0,1,0,0,0,0,0],
# [0,1,1,1,1,1,0],[0,1,1,1,0,0,0]]

visited = [[False]*n for _ in range(n)]
num = 1
count = defaultdict(int)

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:    
        return False
    if not visited[x][y]:
        if graph[x][y] == 1:
            graph[x][y] = num
            count[num] += 1
            visited[x][y] = True

            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            num += 1

print(len(count))
for i in sorted(count.values()):
    print(i)
