import sys
import heapq

T, n = map(int,sys.stdin.readline().split())
heap=[]
 
for _ in range(n):
    id, time, prio = map(int,sys.stdin.readline().split())
    heapq.heappush(heap,[-prio,id,time])

for _ in range(T):
    a = heapq.heappop(heap)
    print(abs(a[1]))
    if a[2]-1 > 0:
        heapq.heappush(heap,[a[0]+1,a[1],a[2]-1])
