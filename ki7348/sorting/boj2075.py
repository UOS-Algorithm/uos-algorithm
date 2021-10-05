import sys
import heapq
n = int(sys.stdin.readline())

graph = []
heap = []
heapq.heapify(heap)

first_arr = list(map(int,sys.stdin.readline().split()))
for i in first_arr:
    heapq.heappush(heap,i)

for _ in range(n-1):
    arr = list(map(int,(sys.stdin.readline().split())))
    heapq.heapify(arr)
    for i in arr:
        a = heapq.heappop(heap)
        if i > a:
            heapq.heappush(heap,i)
        elif i < a:
            heapq.heappush(heap,a)

print(heapq.heappop(heap))