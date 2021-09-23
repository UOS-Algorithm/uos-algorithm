import sys
from collections import deque

def bfs(graph, v, visited):
    result = 0
    queue = deque([1])
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result += 1
    return result

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n+1):
    graph[i].sort()

print(bfs(graph, 1, visited))