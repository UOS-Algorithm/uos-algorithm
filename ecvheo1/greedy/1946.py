import sys

t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] * (n+1)
    count = 1

    for _ in range(n):
        s, m = map(int, sys.stdin.readline().split())
        a[s] = m
    
    minInterview = a[1]
    for i in range(1, n+1):
        if a[i] < minInterview:
            count += 1
            minInterview = a[i]
    print(count)