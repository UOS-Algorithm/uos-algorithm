import sys
import heapq

n = int(sys.stdin.readline())
k = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x:
        if x < 0:
            heapq.heappush(k, (2*abs(x), x))
        else:
            heapq.heappush(k, (2*abs(x)+1, x))

    else:
        if k:
            print(heapq.heappop(k)[1])
        else:
            print(0)