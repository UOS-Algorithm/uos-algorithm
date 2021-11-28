import sys
INF = int(1e9)

m= int(sys.stdin.readline())

list_n = []
temp = []

for _ in range(m):
    query = sys.stdin.readline().split()
    temp.append(query)
    list_n.append(query[0])
    list_n.append(query[-1])
    
list_n = list(set(list_n))

n = len(list_n)

graph=[[INF]*(n)for _ in range(n)]

for i in temp:
    graph[list_n.index(i[0])][list_n.index(i[-1])] = 1

    
for k in range(0,n):
    for a in range(0,n):
        for b in range(0,n):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

case = int(sys.stdin.readline())


for a in range(0,n):
    for b in range(0,n):
        if graph[a][b] == INF:
            graph[a][b] = 0
            


for _ in range(case):
    x = sys.stdin.readline().strip()
    if x[0] in list_n and x[-1] in list_n:
        if graph[list_n.index(x[0])][list_n.index(x[-1])] > 0:
            print('T')
        else:
            print('F')
    else:
        print('F')


        