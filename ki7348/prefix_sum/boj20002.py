import sys

n = int(sys.stdin.readline().strip())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

prefix_sum = [[-1001]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j] = arr[i-1][j-1] + prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1]

max_arr = prefix_sum[0][0]

for k in range(n):
    for i in range(1,n-k+1):
        for j in range(1,n-k+1):
            profit = prefix_sum[i+k][j+k] - prefix_sum[i-1][j+k] - prefix_sum[i+k][j-1] + prefix_sum[i-1][j-1]
            max_arr = max(profit,max_arr)

print(max_arr)