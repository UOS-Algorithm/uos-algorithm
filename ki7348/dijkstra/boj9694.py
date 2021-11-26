import sys
import heapq
INF = int(1e9)

case = int(sys.stdin.readline())

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
                temp[i[0]] = now
                heapq.heappush(q,(cost,i[0]))
    
for x in range(1,case+1):
    m,n = map(int,sys.stdin.readline().split())

    graph = [[] for _ in range(n)]
    distance = [INF] * (n)
    temp = [-1 for _ in range(n)]

    for _ in range(m):
        a,b,c = map(int,sys.stdin.readline().split())
        graph[a].append((b,c))
        graph[b].append((a,c))


    dijkstra(0)
    print(temp)
    result = [n-1]
    idx = n-1
    while temp[idx] != -1:
        idx = temp[idx]
        result.append(idx)
    result.reverse()
    
    if len(result) == 1:
        result = [-1]

    print('Case #{}:'.format(x), *result)

