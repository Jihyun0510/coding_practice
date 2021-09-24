from collections import deque
import sys

# m,n,h = 5,3,2
m,n,h = map(int, input().split())
# graph = [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
# [[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0]]]

graph=[]
for _ in range(h):
    floor = []
    for _ in range(n):
        x = list(map(int, sys.stdin.readline().rstrip().split()))
        floor.append(x)
    graph.append(floor)

q = deque()
already = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i,j,k))
            elif graph[i][j][k] == 0:
                already = False

dx = [0, 0, 0, 0, 1, -1]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 1, -1, 0, 0]

def bfs():
    while q:
        x,y,z = q.popleft()
        # print(x,y,z)
        for i in range(6):
            a = x + dx[i]
            b = y + dy[i]
            c = z + dz[i]
            # print(a,b,c)
            if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c] == 0:
                q.append((a,b,c))
                graph[a][b][c] = graph[x][y][z] + 1
                # print('yes')
if already:
    print(0)
else:
    bfs()
    answer = 0
    check = False
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    check = True
                else:
                    answer = max(answer, graph[i][j][k])
    if check: print(-1)
    else: print(answer-1)

                




