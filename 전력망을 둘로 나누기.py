from collections import deque
def solution(n, wires):
    
    def bfs(graph, start, visited):
        q = deque([start])
        visited[start] = True
        count = 1
        while q:
            v = q.popleft()
            for i in graph[v]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    count += 1
        return count

    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    answer = 1e9
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        visited = [False] * (n+1)
        A = bfs(graph, 1, visited)
        B = n - A
        answer = min(answer, abs(A-B))
        graph[a].append(b)
        graph[b].append(a)
        
    
    return answer