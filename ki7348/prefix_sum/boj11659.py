import sys

n,m = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

prefix_sum = [0]
total = 0

for i in arr:
    total += i
    prefix_sum.append(total)

for _ in range(m):
    i, j = map(int,sys.stdin.readline().split())
    print(prefix_sum[j]-prefix_sum[i-1])