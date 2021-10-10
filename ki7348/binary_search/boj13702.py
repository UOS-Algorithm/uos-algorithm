import sys

n, k = map(int,sys.stdin.readline().split())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

start = 0
end = max(arr)
result = 0

while start <= end:
    total = 0
    mid = (start+end) // 2
    for x in arr:
        total+=x//mid
    if total < k:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)