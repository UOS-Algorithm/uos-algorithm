import sys
import heapq

case = int(sys.stdin.readline())
arr = []
for _ in range(case):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key=lambda x: x[0])
 
heap = [0]
count = 1

for start, end in arr:
    if start >= heap[0]:
        heapq.heappop(heap)
    else:
        count+=1
    heapq.heappush(heap, end)
 
print(count)