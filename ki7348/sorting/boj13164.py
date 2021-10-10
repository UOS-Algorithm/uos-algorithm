import sys
import heapq

n,k = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
heap = []
heapq.heapify(heap)
for i in range(len(arr)-1): # 0 1 2 3 4
    heapq.heappush(heap,(-arr[i+1]+arr[i]))

for i in range(k-1):
    heapq.heappop(heap)

print(abs(sum(heap)))
