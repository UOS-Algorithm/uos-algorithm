import sys
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1

    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if graph[nx][ny] == 0:
                cnt+=1
                queue.append((nx,ny))
                graph[nx][ny] = 1
    return cnt

total = 0
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m,n,k = map(int,sys.stdin.readline().split())

graph = []
for _ in range(m):
    graph.append([0]*n)

for _ in range(k):
    arr = list(map(int,sys.stdin.readline().split()))
    for i in range(m-arr[3],m-arr[1]):
        for j in range(arr[0],arr[2]):
            graph[i][j] = 1


for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            total+=1
            result.append(bfs(i,j))

print(total)

result.sort()
print(' '.join(map(str,result)))