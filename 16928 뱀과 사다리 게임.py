from collections import deque
import sys

n, m = map(int, input().split())
# n, m = 4,9

# moves = {32: 62, 42: 68, 12: 98, 95: 13, 97: 25, 93: 37, 79: 27, 75: 19, 49: 47, 67: 17}
moves = dict()
for _ in range(n+m):
	s, e = map(int,sys.stdin.readline().rstrip().split())
	moves[s] = e

graph = [0] * (100+1)
q = deque()
q.append(1)
while q:
    l = q.popleft()
    for i in range(1, 6+1):
        if i+l <= 100:
            new = i+l
            
        if new in moves:
            new = moves[new]
            
        if graph[new] == 0:
            q.append(new)
            graph[new] = graph[l]+1
print(graph[100])
