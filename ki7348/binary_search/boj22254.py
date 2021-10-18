import sys
import heapq
import copy

n,x = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

start = 1
end = n

while start <= end:

    mid = (start+end) // 2
    total = 0

    heap = []
    heapq.heapify(heap)
    for _ in range(mid):
        heapq.heappush(heap,0)
    
    for i in range(n):
        use = heapq.heappop(heap)
        heapq.heappush(heap,use + arr[i])

    if max(heap) <= x:
        end = mid - 1
    else:
        start = mid + 1
print(start)
