import sys
import heapq
INF = int(1e9)

n,m,total,start = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n)]
distance = [INF] * (n)

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,2*c))
    graph[b].append((a,2*c))

def dijkstra(start):
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

dijkstra(start)

distance.sort()
result = 1

for i in distance:
    if i > total:
        print(-1)
        exit()
temp = 0
for i in distance:
    if temp + i <= total:
        temp+=i
    else:
        result+=1
        temp = i

        
print(result)
    