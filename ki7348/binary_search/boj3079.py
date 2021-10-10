import sys

n,m = map(int,sys.stdin.readline().split())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))


arr.sort()

start = 0
end = max(arr)*m

while start <=  end:
    mid = (start+end)//2
    total = 0

    for x in arr:
        if x <= mid:
            total += mid // x

    if total >= m:
        end = mid-1
    else:
        start = mid+1

print(start)