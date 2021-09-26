import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []

cnt = 0
total = 0

def dfs(x,y):
    global cnt
    
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y] == 1:
        cnt+=1
        graph[x][y] = 0
        for i in range(4):
            dfs(x+dx[i],y+dy[i])
        return True

for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            total+=1
            result.append(cnt)
            cnt = 0

print(total)
result.sort()
for i in result:
    print(i)