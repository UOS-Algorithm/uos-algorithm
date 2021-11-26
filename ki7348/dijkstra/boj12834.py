import sys
import heapq
INF = int(1e9)

person,n,m = map(int,sys.stdin.readline().split())

kist,food = map(int,sys.stdin.readline().split())

team = list(map(int,sys.stdin.readline().split()))

graph = [[] for _ in range(n+1)]

for _ in range(m):
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

result = []
for i in team:
    temp = dijkstra(i,[INF] * (n+1))
    if temp[kist] == INF:
        temp[kist] = -1
    if temp[food] == INF:
        temp[food] = -1
    result.append(temp[kist]+temp[food])


print(sum(result))