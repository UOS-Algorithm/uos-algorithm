import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(person, x,y,color):
    queue = deque()
    queue.append((x,y))
    person[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny>=n:
                continue
            if person[nx][ny] == color:
                person[nx][ny] = 0
                queue.append((nx,ny))

n = int(sys.stdin.readline())
count = 0
count2 = 0

graph = []
graph2 = [[0]*n for _ in range(n)]

for _ in range(n):
    a = list(sys.stdin.readline().strip())
    graph.append(a)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R' or graph[i][j] == 'G':
            graph2[i][j] = 'R'
        else:
            graph2[i][j] = 'B'


for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            bfs(graph,i,j,'R')
            count+=1
        elif graph[i][j] == 'B':
            bfs(graph,i,j,'B')
            count+=1
        elif graph[i][j] == 'G':
            bfs(graph,i,j,'G')
            count+=1


for i in range(n):
    for j in range(n):
        if graph2[i][j] == 'R':
            bfs(graph2,i,j,'R')
            count2+=1
        elif graph2[i][j] == 'B':
            bfs(graph2,i,j,'B')
            count2+=1

result = []

result.append(count)
result.append(count2)

print(' '.join(map(str,result)))
