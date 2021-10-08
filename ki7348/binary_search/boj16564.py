import sys

n,k = map(int,sys.stdin.readline().split())

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
        if x < mid:
            total+=mid-x
    if total > k:
        end = mid-1
    else:
        x += mid-x
        result = mid
        start = mid+1

print(result)