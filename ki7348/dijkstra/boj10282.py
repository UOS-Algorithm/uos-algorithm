import sys
import heapq
INF = int(1e9)

t= int(sys.stdin.readline())

for _ in range(t):
    n,m,k = map(int,sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(m):
        a,b,c = map(int,sys.stdin.readline().split())
        graph[b].append((a,c))

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

    dijkstra(k)
    count = 0
    max_distance = 0
    distance = distance[1:]
    for i in distance:
        if i != INF:
            count+=1
            max_distance=max(max_distance,i)

    print(count,max_distance)