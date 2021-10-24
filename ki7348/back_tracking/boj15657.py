import sys

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

result = []

def back_tracking(index,idx,n,m):
    if index==m:
        print(*result)
        return
    else:
        for k in range(idx,n):
            result.append(arr[k])
            back_tracking(index+1,k,n,m)
            result.pop()
back_tracking(0,0,n,m)
