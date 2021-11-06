import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 2

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if i == 0 and graph[i][j] == 0:
            bfs(i,j)

if 2 in graph[-1]:
    print('YES')
else:
    print('NO')