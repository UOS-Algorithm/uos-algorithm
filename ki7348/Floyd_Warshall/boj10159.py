import sys
INF = int(1e9)

n= int(sys.stdin.readline())
m= int(sys.stdin.readline())


graph=[[INF]*(n+1)for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]=1
    
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a][b]=1

        
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
            
for a in range(1,n+1):
    for b in range(1, n+1):
        if graph[a][b]==INF:
            graph[a][b] = 0
            


for a in range(1,n+1):
    cnt = 0
    temp = []
    for b in range(1, n+1):
        temp.append(max(graph[b][a],graph[a][b]))
    
    for i in temp:
        if i == 0:
            cnt+=1
    print(cnt)
        