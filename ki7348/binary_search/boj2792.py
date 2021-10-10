import sys
from math import ceil

n,m = map(int,sys.stdin.readline().split())

arr = []

for _ in range(m):
    arr.append(int(sys.stdin.readline()))

start = 1
end = max(arr)

while start <= end:
    total = 0
    mid = (start+end) // 2
    for x in arr:
        if x % mid == 0:
            total+=(x//mid)
        else:
            total+=x//mid+1

    if total <= n:
        end = mid-1
    else:
        start = mid+1

print(start)