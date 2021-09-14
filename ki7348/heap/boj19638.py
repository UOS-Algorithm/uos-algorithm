import sys
import heapq

n, h, t = map(int,sys.stdin.readline().split())
count = 0

heap = []
for _ in range(n):
    heapq.heappush(heap,-int(sys.stdin.readline())) 


for i in range(t):
    a = heapq.heappop(heap)
    if abs(a) < h:
        heapq.heappush(heap,a) 
        break
    elif abs(a) == 1:
        heapq.heappush(heap,a)
    else:
        a = -(abs(a)//2)
        heapq.heappush(heap,a) 
        count+=1


if abs(min(heap)) < h:
    print('YES')
    print(count)
else:
    print('NO')
    print(abs(heapq.heappop(heap)))
