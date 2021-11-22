import sys

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

d = [0] * (m)
d[0] = 1
d[1] = 1

for i in range(2,m):
    d[i] = (i)*d[i-1]

print(d[m-1]//(d[m-n]*d[n-1]))