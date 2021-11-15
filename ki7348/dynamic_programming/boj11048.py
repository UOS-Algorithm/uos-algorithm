import sys

n, m = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

d = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        d[i][j] = max(d[i-1][j]+arr[i][j],d[i][j-1]+arr[i][j])

print(d[n-1][m-1])