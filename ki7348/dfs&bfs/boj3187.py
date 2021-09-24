import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y,wolf,sheep):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0


    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx>=r or ny>=c:
                continue
            if graph[nx][ny] == 'k':
                graph[nx][ny] = 0
                queue.append((nx,ny))
                sheep+=1
            elif graph[nx][ny] == 'v':
                graph[nx][ny] = 0
                queue.append((nx,ny))
                wolf+=1
            elif graph[nx][ny] == '.':
                graph[nx][ny] = 0
                queue.append((nx,ny))

    if sheep > wolf:
        result[0] += sheep
    else:
        result[1] += wolf

r, c =map(int,sys.stdin.readline().split())

graph = []
result = [0, 0]


for i in range(r):
    graph.append(list(sys.stdin.readline().strip()))
k = 0
v = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] == '.':
            bfs(i,j,0,0)
        elif graph[i][j] == 'k':
            bfs(i,j,0,1)
        elif graph[i][j] == 'v':
            bfs(i,j,1,0)
            

print(*result)

