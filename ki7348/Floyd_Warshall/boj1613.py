import sys
INF = int(1e9)

n,m = map(int,sys.stdin.readline().split())

graph=[[INF]*(n+1)for _ in range(n+1)]
graph2=[[INF]*(n+1)for _ in range(n+1)]

    
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a][b]=1
    graph2[b][a]=1

        
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
            graph2[b][a]=min(graph2[b][a], graph2[b][k]+graph2[k][a])
        
        

case = int(sys.stdin.readline())

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            graph[a][b] = 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph2[a][b] == INF:
            graph2[a][b] = 0

for _ in range(case):
    a,b = map(int,sys.stdin.readline().split())
    if graph[a][b] == 0 and graph2[a][b] == 0:
        print(0)
    elif graph[a][b] > 0:
        print(-1)
    elif graph2[a][b] > 0:
        print(1)
    
    
        