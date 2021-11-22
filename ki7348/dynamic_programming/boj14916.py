import sys

n = int(sys.stdin.readline())

d = [0]*(100001)


d[1] = -1
d[2] = 1
d[3] = -1
d[4] = 2
d[5] = 1
d[6] = 3
d[7] = 2
d[8] = 4
d[9] = 3

for i in range(10,100001):
    d[i] = d[i-5]+1

print(d[n])