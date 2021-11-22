import sys

n = int(sys.stdin.readline())

d = [0]*(n+1)

d[0] = 1

for i in range(1,n+1):
    for j in range(i):
        d[i] += d[j]*d[i-j-1]
        
print(d[n])

