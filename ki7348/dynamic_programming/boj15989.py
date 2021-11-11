import sys

case = int(sys.stdin.readline())

for _ in range(case):
    x = int(sys.stdin.readline())

    d = [1] * 10001

    for i in range(2,10001):
        d[i] += d[i-2]
    for i in range(3,10001):
        d[i] += d[i-3]

    d = [0] + d
    print(d[x+1])