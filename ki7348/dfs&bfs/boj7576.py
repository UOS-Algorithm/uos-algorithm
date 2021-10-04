import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(arr):
    queue = deque()
    for i in arr:
        queue.append((i[0],i[1]))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

m,n = map(int,sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
 
start = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            start.append((i,j))

bfs(start)
flag = False
for i in graph:
    if 0 in i:
        flag = True


if flag == True:
    print(-1)
else:
    print(max(map(max,graph))-1)