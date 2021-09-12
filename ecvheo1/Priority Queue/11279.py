import sys
import heapq

n = int(sys.stdin.readline())
maxHeap = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(maxHeap, (-x, x))
    else:
        if maxHeap:
            print(heapq.heappop(maxHeap)[1])
        else:
            print(0)