import sys

n,c = map(int,sys.stdin.readline().split())
# 1 2 4 8 9

arr =[]

for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()


start = 1
end = arr[-1] - arr[0]

while start <= end:
    mid = (start+end)//2 #4
    total = 1
    initial = arr[0]

    for x in arr:
        if x >= initial + mid:
            total+=1
            initial = x

    if total < c:
        end = mid-1
    else:
        start = mid+1


print(start-1)