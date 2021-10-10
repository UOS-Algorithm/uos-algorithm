import sys

n, m =map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
start = 0
end = 1e12
result = 0

while start <= end:
    total = 0
    mid = (start+end) // 2
    for x in arr:
        total+=mid//x
    if total >= m:
        end = mid-1
    else:
        result = mid+1
        start = mid+1

print(int(result))