import sys
INF = int(1e9)

n = int(sys.stdin.readline())

graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

    
for a in range(n):
    for b in range(n):
        if graph[a][b] == 0:
            graph[a][b] = INF

        
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])


for a in range(n):
    for b in range(n):
        if graph[a][b]==INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()
        