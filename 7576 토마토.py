from collections import deque
import sys
# m, n = 6,4
# graph = [[0,0,0,0,0,0], [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,1]]

already = False
q = deque()
# q.append((3,5))

m, n = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())) )
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))
        elif graph[i][j] == 0 and already:
             already=False

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if n>a>=0 and 0<=b<m and graph[a][b]==0:
                q.append((a,b))
                graph[a][b] = graph[x][y] + 1
if already:
    print(0)
else:
    answer = 0
    check = False
    bfs()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                check = True
            answer = max(answer, graph[i][j])
            
    if check:
        print(-1)
    else: print(answer-1)
            


