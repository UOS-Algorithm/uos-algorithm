import sys
INF = int(1e9)

n= int(sys.stdin.readline())

graph=[[INF]*(n+1)for _ in range(n+1)]

    
while True:
    a,b=map(int,sys.stdin.readline().split())
    if a==-1 and b==-1:
        break
    graph[a][b]=1
    graph[b][a]=1

for a in range(1,n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]=0
                   
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
result = []
for i in range(1,n+1):
    max_val = 0
    for j in range(1,n+1):
        max_val = max(max_val,graph[i][j])        
    result.append(max_val)

min_result = min(result)
count = 0   
pre = []
for i in range(len(result)):
    if result[i] == min_result:
        pre.append(i+1)
        count+=1
        
print(min_result, count)
print(*pre)