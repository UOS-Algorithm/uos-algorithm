import sys
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 1:
                cnt+=1
                queue.append((nx,ny))
                graph[nx][ny] = 0
    return cnt


total = 0
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int,sys.stdin.readline().split())


graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            total +=1 
            result.append(bfs(i,j))

print(total)
if result:
    print(max(result))
else:
    print(0)