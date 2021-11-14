import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

d = [0] * (n+1)

for i in range(1,n+1):
    if arr[-i][0] <= i:
        d[i] = max(d[i-arr[-i][0]]+arr[-i][1],d[i-1])
    else:
        d[i] = d[i-1] 

print(d[-1])