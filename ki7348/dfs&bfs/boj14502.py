import sys
from collections import deque
from itertools import combinations
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


n, m = map(int,sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))



zero_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_list.append([i,j])

comb_zero_list = list(combinations(zero_list,3))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if temp_graph[nx][ny] == 0:
                queue.append((nx,ny))
                temp_graph[nx][ny] = 2
arr=[]
for comb in comb_zero_list:
    count = 0
    temp_graph = copy.deepcopy(graph)
    temp_graph[comb[0][0]][comb[0][1]] = 1 
    temp_graph[comb[1][0]][comb[1][1]] = 1
    temp_graph[comb[2][0]][comb[2][1]] = 1
    
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2:
                bfs(i,j)
    
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 0:
                count+=1

    arr.append(count)

print(max(arr))
