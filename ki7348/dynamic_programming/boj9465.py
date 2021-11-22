import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]
    
    d = [[0]*n for _ in range(2)]
    
    if n == 1:
        print(max(arr[0][0],arr[1][0]))
    else:
        d[0][0] = arr[0][0]
        d[1][0] = arr[1][0]
        
        d[0][1] = d[1][0]+arr[0][1]
        d[1][1] = d[0][0]+arr[1][1]
        
        for i in range(2,n):
            d[0][i] = max(d[1][i-1],d[1][i-2])+arr[0][i]
            d[1][i] = max(d[0][i-2],d[0][i-1])+arr[1][i]
        print(max(d[0][-1],d[1][-1]))