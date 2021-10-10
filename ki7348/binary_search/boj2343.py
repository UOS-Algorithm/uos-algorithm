import sys

n,m = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

start = max(arr)
end = sum(arr)

while start <= end:
    total = 0
    count = 0
    mid = (start+end) // 2
    for x in arr:
        if x > mid or total + x > mid:
            count +=1 
            total = 0
        total += x


    if count < m:
        end = mid-1
    else:
        start = mid+1


print(start)

