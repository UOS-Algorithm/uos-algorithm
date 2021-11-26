import sys
INF = int(1e9)

n,m = map(int,sys.stdin.readline().split())


graph=[[INF]*(n+1)for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]=0
    
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    if graph[a][b]>c:
        graph[a][b]=c
        graph[b][a]=c

        
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])


for i in range(0,n+1):
    for j in range(0,n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
            
result = []

for i in range(1,n+1):
    result.append(sum(graph[i]))

print(result.index(min(result))+1)
        