import sys
INF = int(1e9)

n = int(sys.stdin.readline())


graph=[[INF]*(n+1)for _ in range(n+1)]

arr = []
for _ in range(n):
    s,e = map(int,sys.stdin.readline().split())
    arr.append([s,e])


for i in range(n):
    for j in range(i+1,n):
        if arr[i][1] >= arr[j][0] and arr[j][1] >= arr[i][0]:
            graph[i+1][j+1] = 1
            graph[j+1][i+1] = 1
        else:
            graph[i+1][j+1] = INF

        
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])


case = int(sys.stdin.readline())

for _ in range(case):
    x,y = map(int,sys.stdin.readline().split())
    if graph[x][y] != INF:
        print(graph[x][y])
    else:
        print(-1)
    
        