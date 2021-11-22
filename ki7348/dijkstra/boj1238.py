import sys
import heapq
INF = int(1e9)

n,m,x = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
# distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

arr = []
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


for start in range(1,n+1):
    arr.append(dijkstra(start,[INF] * (n+1)))

result = [0]*(n)

for i in range(n):
    result[i] += arr[i][x]
    result[i] += arr[x-1][i+1]
    
print(max(result))