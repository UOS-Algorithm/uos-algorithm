import sys

n,m = map(int,sys.stdin.readline().split())

case = int(sys.stdin.readline())

arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

prefix_sum = [[[0,0,0] for i in range(m+1)] for j in range(n+1)] 


for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i-1][j-1] == 'J':
            prefix_sum[i][j][0] = 1 + prefix_sum[i][j-1][0] + prefix_sum[i-1][j][0] - prefix_sum[i-1][j-1][0]
        else:
            prefix_sum[i][j][0] = prefix_sum[i][j-1][0] + prefix_sum[i-1][j][0] - prefix_sum[i-1][j-1][0]

for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i-1][j-1] == 'O':
            prefix_sum[i][j][1] = 1 + prefix_sum[i][j-1][1] + prefix_sum[i-1][j][1] - prefix_sum[i-1][j-1][1]
        else:
            prefix_sum[i][j][1] = prefix_sum[i][j-1][1] + prefix_sum[i-1][j][1] - prefix_sum[i-1][j-1][1]

for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i-1][j-1] == 'I':
            prefix_sum[i][j][2] = 1 + prefix_sum[i][j-1][2] + prefix_sum[i-1][j][2] - prefix_sum[i-1][j-1][2]
        else:
            prefix_sum[i][j][2] = prefix_sum[i][j-1][2] + prefix_sum[i-1][j][2] - prefix_sum[i-1][j-1][2]

for i in range(case):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    a = prefix_sum[x2][y2][0]-prefix_sum[x1-1][y2][0]-prefix_sum[x2][y1-1][0]+prefix_sum[x1-1][y1-1][0]
    b = prefix_sum[x2][y2][1]-prefix_sum[x1-1][y2][1]-prefix_sum[x2][y1-1][1]+prefix_sum[x1-1][y1-1][1]
    c = prefix_sum[x2][y2][2]-prefix_sum[x1-1][y2][2]-prefix_sum[x2][y1-1][2]+prefix_sum[x1-1][y1-1][2]
    print(a,b,c)