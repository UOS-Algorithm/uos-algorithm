import sys

n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

start = min(arr)
end = sum(arr)

while start <= end:
    total = 0
    count = 0
    mid = (start+end)//2

    for x in arr:
        total+=x
        if total >= mid:
            total = 0
            count+=1


    if count < k:
        end = mid - 1
    else:
        start = mid + 1

print(end)
