import sys

n,m = map(int,sys.stdin.readline().split())

d = [0] * 101

d[1] = 1

for i in range(2,101):
    d[i] = i*d[i-1]

print(d[n]//(d[n-m]*d[m]))