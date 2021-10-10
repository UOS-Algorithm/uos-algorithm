import sys

n, l = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

count = 0

cur = arr[0]
newarr=[]
for i in arr:
    if i - cur <= l-1:
        newarr.append(i)
    else:
        count+=1
        newarr.clear()
        newarr.append(i)
        cur = i

if newarr:
    print(count+1)
else:
    print(count)