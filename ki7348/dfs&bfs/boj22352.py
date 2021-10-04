import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    k = 0
    k = graph[x][y]
    graph[x][y] = graph2[x][y]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == k:
                graph[nx][ny] = graph[x][y]
                queue.append((nx,ny))

n, m = map(int,sys.stdin.readline().split())

graph = []
graph2 = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    graph2.append(list(map(int,sys.stdin.readline().split())))

flag = True
for i in range(n):
    for j in range(m):
        if graph[i][j] != graph2[i][j]:
            bfs(i,j)
            flag = False
    if flag==False:
        break

if graph == graph2:
    print('YES')
else:
    print('NO')

