n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

#플로이드 워셜
for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

#출력
for a in range(n):
    for b in range(n):
        print(graph[a][b], end=" ")
    print()