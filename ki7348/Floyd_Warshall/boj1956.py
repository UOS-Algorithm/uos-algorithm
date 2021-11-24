import sys
INF = int(1e9)

n,m = map(int,sys.stdin.readline().split())


graph=[[INF]*(n+1)for _ in range(n+1)]


    
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    if graph[a][b]>c:
        graph[a][b]=c

        
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

result = []

for i in range(1,n+1):
    result.append(graph[i][i])
    
if min(result) != 1e9:
    print(min(result))
else:
    print(-1)
