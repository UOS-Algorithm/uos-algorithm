import sys

case = int(sys.stdin.readline())

d = [0] * 11

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4,11):
    d[i] = d[i-2]+d[i-1]+d[i-3]

for _ in range(case):
    x = int(sys.stdin.readline())
    print(d[x])