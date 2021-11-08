import sys
import math

n = int(sys.stdin.readline())

d = [x for x in range(n+1)]


for i in range(4,n+1):
    for j in range(1,i):
        if j*j>i:
            break
        if d[i] > d[i-j*j]+1:
            d[i] = 1 + d[(i-j*j)]

print(d[n])