from collections import deque
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

puzzles = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()   
    q.append([x,y])
    puzzle = [[0,0]]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(table) and 0 <= ny < len(table):
                if table[nx][ny] == 1:
                    q.append([nx, ny])
                    puzzle.append([dx, dy])
                    table[nx][ny] = 0
    return puzzle
for i in range(len(table)):
    for j in range(len(table)):
        if table[i][j]:
            puzzles.append(bfs(i, j))
print(puzzles)    

