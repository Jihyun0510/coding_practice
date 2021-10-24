import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

routes = [
    # 도형1
    [(0,1), (0,1),(0,1)],
    # 도형2
    [(0,1),(-1,0),(0,-1)],
    # 도형3
    [(-1,0),(-1,0),(0,-1)],
    [(-1,0),(-1,0),(0,1)],
    [(0,-1),(-1,0),(-1,0)],
    [(0,1),(-1,0),(-1,0)],
    # 도형4
    [(-1,0),(0,1),(-1,0)],
    [(-1,0),(0,-1),(-1,0)],
    # 도형5
    [(0,1),(0,1),(-1,-1)],
    [(0,1),(0,1),(1,-1)]
]

answer = 0

def find_sum_x(x, y, route):
    count = 0
    count += graph[x][y]

    for r in route:
        x += r[0]
        y += r[1]

        if 0 <= x < n and 0 <= y < m:
            count += graph[x][y]
        else:
            return 0
    return count


def find_sum_y(x, y, route):
    count = 0
    count += graph[x][y]

    for r in route:
        x += r[1]
        y += r[0]

        if 0 <= x < n and 0 <= y < m:
            count += graph[x][y]
        else:
            return 0
    return count        

for i in range(n):
    for j in range(m):
        for route in routes:
            answer = max(answer, find_sum_x(i, j, route))
            answer = max(answer, find_sum_y(i, j, route))

print(answer)
