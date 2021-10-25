import sys

n,m = map(int,sys.stdin.readline().split())

result = []
visited = [False]*n

def back_tracking(index,idx,n,m):
    if index==m:
        print(*result)
        return
    else:
        for k in range(idx,n):
            if not visited[k]:
                visited[k]=True
                result.append(k+1)
                back_tracking(index+1,k,n,m)
                visited[k]=False
                result.pop()
back_tracking(0,0,n,m)
