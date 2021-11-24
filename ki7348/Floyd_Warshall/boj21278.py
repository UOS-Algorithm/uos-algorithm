import sys
INF = int(1e9)

n,m = map(int,sys.stdin.readline().split())


graph=[[INF]*(n+1)for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]=0
    
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a][b]=2
    graph[b][a]=2

        
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
            

result = []
h = 0
for a in range(2,n+1):
    for b in range(1, a):
        temp = []
        for c in range(1,n+1):
            temp.append(min(graph[a][c],graph[b][c]))
            h = sum(temp)
        first = min(a,b)
        second = max(a,b)
        result.append([first,second,h])
        
result.sort(key=lambda x:x[2])
print(*result[0])