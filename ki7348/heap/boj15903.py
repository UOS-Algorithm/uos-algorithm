import sys
import heapq

n, m = map(int,sys.stdin.readline().split())

heap = []

arr = list(map(int,sys.stdin.readline().split()))

for i in arr:
    heapq.heappush(heap, i)

for i in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap,a+b)
    heapq.heappush(heap,a+b)

print(sum(heap))