import sys
import heapq
INF = int(1e9)

n,m,r = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
item = list(map(int,sys.stdin.readline().split()))
# distance = [INF] * (n+1)

for _ in range(r):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dijkstra(start,distance):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance
result = [0] * (n+1)

for i in range(1,n+1):
    temp = dijkstra(i,[INF] * (n+1))
    temp = temp[1:]
    for j in range(n):
        if temp[j] <= m:
            result[i]+=item[j]
            

print(max(result))