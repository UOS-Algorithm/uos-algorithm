import sys
from collections import deque

def bfs(graph,visited):
    queue = deque([1])
    visited[1] = True
    total = [0]*(n+1)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                total[i] = total[v]+1
                queue.append(i)
                visited[i] = True
    return total

n, m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]


for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

result = bfs(graph,[False]*(n+1))

a = result.index(max(result))
b = result[a]
c = result.count(max(result))

print(a,b,c)