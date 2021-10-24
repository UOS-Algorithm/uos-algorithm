import sys

n,m = map(int,sys.stdin.readline().split())

result = []

def back_tracking(index,idx,n,m):
    if index==m:
        print(*result)
        return
    else:
        for k in range(idx, n):
            result.append(k+1)
            back_tracking(index+1,k,n,m)
            result.pop()
back_tracking(0,0,n,m)
