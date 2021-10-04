import sys
from collections import deque

def bfs(graph,start):
    queue = deque([start])
    visited[start] = True
    total = [0]*(n+1)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                total[i] = total[v]+1
                queue.append(i)
                visited[i] = True
    return sum(total)

n, m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
result = [0]*(n+1)


for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
        visited = [False]*(n+1)
        result[i] = (bfs(graph,i))

print(result.index(min(result[1:])))