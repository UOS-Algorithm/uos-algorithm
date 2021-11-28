import sys
INF = int(1e9)

n,m = map(int,sys.stdin.readline().split())


graph=[[INF]*(n+1)for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

    
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    if c == 0:
        graph[a][b] = 0
        graph[b][a] = 1
    else:
        graph[a][b] = 0
        graph[b][a] = 0
        
        
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])


case = int(sys.stdin.readline())

for _ in range(case):
    x,y = map(int,sys.stdin.readline().split())
    print(graph[x][y])

