# direction: north=0, east=1, south=2, west=3
from collections import deque

def direction(oper, d):
    
    if oper == 'L': 
        d = (d-1)%4
    elif oper == 'R': 
        d = (d+1)%4
    return d
    
def bfs(x, y, d, width, height, graph, grid):
    
    count = 0
    start = [x, y, d]
    while True:
        # add current node to Visited
        if graph[x][y][d]:
            ans = count
            count = 0
            return ans
        graph[x][y][d] = 1
        count += 1
        
        # Move
        # to North
        if d == 0:
            x = (x+1)%height
        # to East
        elif d == 1:
            y = (y+1)%width
        # to South
        elif d ==2:
            x = (x-1)%height
        # to West
        else:
            y = (y-1)%width
        
        # change direction
        d = direction(grid[x][y], d)
        
def solution(grid):
    graph = [[[0, 0, 0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    answer = []
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                if graph[i][j][k] != 1:
                    num = bfs(i, j, k, len(grid[0]), len(grid), graph, grid)
                    answer.append(num)
    answer.sort()
    return answer