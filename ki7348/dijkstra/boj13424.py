import sys
import heapq
INF = int(1e9)

case = int(sys.stdin.readline())

for _ in range(case):
    n,m = map(int,sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b,c = map(int,sys.stdin.readline().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    k = int(sys.stdin.readline())
    k_list = list(map(int,sys.stdin.readline().split()))

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
    for i in k_list:
        result.append(dijkstra(i,[INF] * (n+1)))
    dis = [0]*(n+1)
    for i in range(1,n+1):
        for j in result:
            dis[i]+=j[i]
            
    dis = dis[1:]
    min_dis = min(dis)
    for i in range(0,n):
        if dis[i] == min_dis:
            print(i+1)
            break