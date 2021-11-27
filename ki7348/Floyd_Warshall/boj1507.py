import sys
INF = int(1e9)

n = int(sys.stdin.readline())

result = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

temp = 0
graph=[[1]*(n)for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if k == a or a == b or k == b:
                continue
            if result[a][b] == result[a][k] + result[k][b]:
                graph[a][b] = 0
            elif result[a][b] > result[a][k] + result[k][b]:
                temp = -1

if temp == -1:
    print(-1)
    exit()
else:
    for i in range(n):
        for j in range(i,n):
            if graph[i][j]==1:
                temp+=result[i][j]
            
print(temp)




        