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

        
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

case = int(sys.stdin.readline())
friend = list(map(int,sys.stdin.readline().split()))

result = []
for i in range(1,n+1):
    temp = []
    for j in friend:
        temp.append(graph[j][i]+graph[i][j])
    result.append(max(temp))
    
min_result = min(result)
final = []
for i in range(len(result)):
    if result[i] == min_result:
        final.append(i+1)
        
        
print(*final)