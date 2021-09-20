import sys
import heapq

case = int(sys.stdin.readline())


for i in range(case):
    page = int(sys.stdin.readline())
    heap=list(map(int,sys.stdin.readline().split()))
    heapq.heapify(heap)
    sum = 0
    for j in range(page-1):
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        sum += a + b
        heapq.heappush(heap,a+b)
    print(sum)
