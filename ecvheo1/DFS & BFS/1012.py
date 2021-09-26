import sys
from collections import deque

def bfs(x, y):
    if graph[x][y] != 1:
        return False
    else:
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if graph[nx][ny] == 0:
                    continue
                else: # graph[nx][ny] == 1
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
        return True

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    result = 0
    for i in range(n):
       for j in range(m):
           if bfs(i, j) == True:
               result += 1
    print(result) 