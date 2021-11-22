import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

d = [0] * n
d[1] = max(arr[0:2])-min(arr[0:2])

for i in range(2,n): # 3
    for j in range(i): # 0 1 2
        temp = d[j]+(max(arr[j+1:i+1])-min(arr[j+1:i+1]))
        d[i] = max(d[i],temp)


print(max(d))