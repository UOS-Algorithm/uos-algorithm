import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y,visited):
    queue = deque()
    queue.append((x,y))
    

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph
n,m = map(int,sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

flag = True
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            graph[i][j] = 0
            bfs(i,j,visited)
            flag = False
            break
    if flag == False:
        break

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            graph[i][j] = -1

for x in range(n):
    print(' '.join(map(str,graph[x])))