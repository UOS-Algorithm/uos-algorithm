import sys
from collections import deque

def ripen(graph):
    for i in range(n):
        if 0 in graph[i]:
            return False
    return True

def bfs(q, time):
    while q:
        time += 1
        for _ in range(len(q)):
            a, b = q.popleft()

            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 0:
                    q.append((nx, ny))
                    graph[nx][ny] = 1
    return time
                    

m, n = map(int, sys.stdin.readline().split())
check = True
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

if ripen(graph):
    check = False
    print(0)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = -1
q = deque() # 익은 토마토 큐

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

if check:
    time = bfs(q, time)
    for i in graph:
        if 0 in i:
            print(-1)
            check = False
            break

if check:
    print(time)