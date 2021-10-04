import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y,color):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx>=m or ny>=n:
                continue
            if graph[nx][ny] == color:
                cnt+=1
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return cnt

n, m = map(int,sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(m)]

sumW = 0
sumB = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W':
            sumW += pow(bfs(i,j,'W'),2)
        elif graph[i][j] == 'B':
            sumB += pow(bfs(i,j,'B'),2)

print(sumW, sumB)