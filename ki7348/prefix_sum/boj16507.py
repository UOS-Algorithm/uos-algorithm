import sys

r,c,k = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(r)]

prefix_sum = [[0]*(c+1) for _ in range(r+1)]

for i in range(1,r+1):
    for j in range(1,c+1):
        prefix_sum[i][j] = arr[i-1][j-1] + prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1]

for i in range(k):
    r1,c1,r2,c2 = map(int,sys.stdin.readline().split())
    sum = prefix_sum[r2][c2]-prefix_sum[r1-1][c2]-prefix_sum[r2][c1-1]+prefix_sum[r1-1][c1-1]
    print(sum // ((r2-r1+1)*(c2-c1+1)))
