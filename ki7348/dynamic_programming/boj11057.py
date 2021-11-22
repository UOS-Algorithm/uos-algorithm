import sys

n = int(sys.stdin.readline())

d = [[0]*10 for _ in range(n+1)]

for i in range(0,10):
    d[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        for k in range(j+1):
            d[i][j] += d[i-1][k]
            
            
print(sum(d[-1])%10007)