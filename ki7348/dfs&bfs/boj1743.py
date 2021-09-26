import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 1:
                cnt+=1
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return cnt

n,m,k = map(int,sys.stdin.readline().split())

graph=[]

for _ in range(n):
    graph.append([0]*m)

for _ in range(k):
    x,y = map(int,sys.stdin.readline().split())
    graph[x-1][y-1] = 1

result=[]

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            result.append(bfs(i,j))
            

print(max(result))


