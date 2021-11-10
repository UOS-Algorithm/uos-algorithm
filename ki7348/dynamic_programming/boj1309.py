import sys

n = int(sys.stdin.readline())

d0 = [0]*(n+1) #no
d1 = [0]*(n+1) #left
d2 = [0]*(n+1) #right

d0[0] = 1

for i in range(1,n+1):
    d0[i] = (d0[i-1]+d1[i-1]+d2[i-1])%9901
    d1[i] = (d0[i-1]+d2[i-1])%9901
    d2[i] = (d0[i-1]+d1[i-1])%9901

print((d0[n]+d1[n]+d2[n])%9901)

