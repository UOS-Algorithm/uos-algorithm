import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

d1 = [0] * n
d2 = [0] * n

d1[0] = 1
d2[0] = 1

for i in range(1,n):
    if arr[i] >= arr[i-1]:
        d1[i] += d1[i-1] + 1
    else:
        d1[i] = 1
for i in range(1,n):
    if arr[i] <= arr[i-1]:
        d2[i] += d2[i-1] + 1
    else:
        d2[i] = 1
       
print(max(max(d1),max(d2)))