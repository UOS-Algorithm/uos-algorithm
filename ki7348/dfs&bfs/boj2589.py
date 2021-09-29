import sys
from collections import deque
from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y,graph):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    max_graph = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 'L':
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                max_graph = max(max_graph,graph[nx][ny])
    return max_graph
n,m = map(int,sys.stdin.readline().split())

graph = []


for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))

result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            temp = []
            temp_graph = deepcopy(graph)
            result.append(bfs(i,j,temp_graph))
            

print(max(result))