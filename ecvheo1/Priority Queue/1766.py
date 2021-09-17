import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

seq = [[] for _ in range(n+1)]
degree = [ 0 for _ in range(n+1) ]
q = []
result = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    seq[a].append(b)
    degree[b] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        heapq.heappush(q, i)

while q:
    now = heapq.heappop(q)
    result.append(now)
    for i in seq[now]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(q, i)

print(*result)