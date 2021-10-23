import sys
from collections import deque
from itertools import combinations
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(visited,temp_graph,arr):
    queue = deque()
    for i in arr:
        queue.append((i[0],i[1]))
        temp_graph[i[0]][i[1]] = 0
        visited[i[0]][i[1]] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny>=n:
                continue
            if ( temp_graph[nx][ny] == 0 or temp_graph[nx][ny] == 2 ) and visited[nx][ny] == False:
                visited[nx][ny] = True
                temp_graph[nx][ny] = temp_graph[x][y] + 1
                queue.append((nx,ny))


n, m = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

temp = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            temp.append((i,j))


comb_list = list(combinations(temp,m))

min_graph = n**2
for comb in comb_list:
    temp_graph = copy.deepcopy(graph)
    visited = [[False]*n for _ in range(n)]
    zero_count = 0
    two_count = 0

    for i in range(n):
        for j in range(n):
            if temp_graph[i][j] == 0:
                zero_count+=1
            if temp_graph[i][j] == 2:
                two_count += 1

    if zero_count == 0 and two_count <= m:
        print(0)
        exit()

    bfs(visited,temp_graph,comb)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if temp_graph[i][j] == 0:
                cnt+=1
    
    if cnt > m:
        continue
    
    
    min_graph = min(min_graph,(max(map(max,temp_graph))))
if min_graph == n**2:
    print(-1)
else:
    print(min_graph)