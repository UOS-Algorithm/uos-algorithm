import sys

n = int(sys.stdin.readline())

d = [0]*n

arr = list(map(int,sys.stdin.readline().split()))

d[0]=arr[0]

for i in range(1,n):
    d[i] = max(arr[i],arr[i]+d[i-1])

print(max(d))
