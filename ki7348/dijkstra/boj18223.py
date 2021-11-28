import sys
import heapq
INF = int(1e9)

n,m,p = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start,end):
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
                
    return distance[end]
if dijkstra(1,n) == dijkstra(1,p) + dijkstra(p,n):
    print('SAVE HIM')
else:
    print('GOOD BYE')
