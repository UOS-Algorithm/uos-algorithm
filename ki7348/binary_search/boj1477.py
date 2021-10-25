import sys

n,m,l = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
arr.append(0)
arr.append(l)

arr.sort()
start = 1
end = l


while start<=end:
    total = 0
    mid = (start+end) // 2

    for x in range(len(arr)-1):
        if arr[x+1]-arr[x] > mid:
            total+=(arr[x+1]-arr[x]-1)//mid

    if total <= m:
        end = mid -1
    else:
        start = mid +1

print(start)
