import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

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
            if graph[nx][ny] == '#':
                graph[nx][ny] = 0
                queue.append((nx,ny))

case = int(sys.stdin.readline())

for _ in range(case):
    n, m = map(int,sys.stdin.readline().split())
    count = 0
    graph = []

    for i in range(n):
        graph.append(list(sys.stdin.readline().strip()))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '#':
                bfs(i,j)
                count+=1

    print(count)