import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



n,k = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

s,target_x,target_y = map(int,sys.stdin.readline().split())

temp = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            temp.append((graph[i][j],i,j,0))

temp.sort()
temp = deque(temp)

    
while temp:
    virus, x, y, time = temp.popleft()
    if time == s:
        break

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx < 0 or ny < 0 or nx>=n or ny>=n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            temp.append((virus, nx, ny, time+1))


print(graph[target_x-1][target_y-1])