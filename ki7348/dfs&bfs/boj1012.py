import sys
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))

case = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(case):
    graph = []
    cnt = 0
    m,n,k = map(int,sys.stdin.readline().split())
    
    for i in range(n):
        graph.append([0]*m)

    
    for j in range(k):
        x, y = map(int,sys.stdin.readline().split())
        graph[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt+=1
                bfs(i,j)
    
    print(cnt)