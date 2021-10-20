from collections import deque
import sys
input = sys.stdin.readline
# n = 5
n = int(input())
graph = [list(input()) for _ in range(n)]
# graph = [['R', 'R', 'R', 'B', 'B'], ['G', 'G', 'B', 'B', 'B'], ['B', 'B', 'B', 'R', 'R'], ['B', 'B', 'R', 'R', 'R'], ['R', 'R', 'R', 'R', 'R']]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()   
    visited[x][y] = True
    q.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[x][y] == graph[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = True
normal = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            normal += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

patient = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:

            bfs(i,j)
            patient += 1
print(normal, patient)
