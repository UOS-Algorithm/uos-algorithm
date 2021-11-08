import sys

case = int(sys.stdin.readline())

d = [0]*68

d[0] = 1
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4,68):
    d[i] = d[i-1] + d[i-2] + d[i-3] + d[i-4]

for _ in range(case):
    x = int(sys.stdin.readline())

    print(d[x])