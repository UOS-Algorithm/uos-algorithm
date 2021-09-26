import sys

vertex, edge = map(int,sys.stdin.readline().split())

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

graph=[[] for _ in range(vertex+1)]
visited = [False] * (vertex+1)
count = 0

for _ in range(edge):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,vertex+1):
    if not visited[i]:
        dfs(i)
        count+=1



print(count)