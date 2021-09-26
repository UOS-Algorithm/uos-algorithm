import sys
import heapq

n = int(sys.stdin.readline())
minHeap = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(minHeap, x)
    else:
        if minHeap:
            print(heapq.heappop(minHeap))
        else:
            print(0)