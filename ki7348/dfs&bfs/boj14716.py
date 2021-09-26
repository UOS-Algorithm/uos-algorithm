import sys
sys.setrecursionlimit(100000)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [0, -1, 1, -1, 1, -1, 0, 1]

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(8):
            dfs(x+dx[i],y+dy[i])
        return True



n, m = map(int,sys.stdin.readline().split())

graph = []
total = 0
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            total+=1 

print(total)