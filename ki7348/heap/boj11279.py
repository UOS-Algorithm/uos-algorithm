import sys
import heapq

case = int(sys.stdin.readline())
heap=[]
for _ in range(case):
    x = int(sys.stdin.readline())
    if x != 0:
       heapq.heappush(heap,-x)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap)) 