import sys
import heapq

case = int(sys.stdin.readline())

heap = []
arr = []
result = 0

heapq.heapify(heap)
for _ in range(case):
    a, b = map(int,sys.stdin.readline().split())
    arr.append([a,b])
arr.sort(key=lambda x:x[1])

for i in arr:
    heapq.heappush(heap,i[0])
    if len(heap)>i[1]:
        heapq.heappop(heap)

print(sum(heap))