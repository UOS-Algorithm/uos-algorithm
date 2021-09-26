import sys
import copy
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    temp_graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny>=n:
                continue
            if temp_graph[nx][ny] > th:
                temp_graph[nx][ny] = 0
                queue.append((nx,ny))
                


n = int(sys.stdin.readline())

graph = []
result = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0


for th in range(0, max(map(max, graph))+1):
    temp_graph = copy.deepcopy(graph)
    total = 0
    for i in range(n):
        for j in range(n):
            if temp_graph[i][j] > th:
                bfs(i,j)
                total+=1
    if total >= answer:
        answer = total

print(answer)


