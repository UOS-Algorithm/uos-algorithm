import sys

n = int(sys.stdin.readline())
a, b = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

def dfs(a, b, count):
    visited[a] = True
    if a == b:
        print(count)
        return
    count+=1
    for i in graph[a]:
        if not visited[i]:
            dfs(i, b, count)

graph=[[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0


for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


dfs(a, b, count)
if visited[b] == False:
    print(-1)