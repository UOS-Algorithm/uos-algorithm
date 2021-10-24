import sys

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

result = []
visited = [False]*(max(arr)+1)

def back_tracking(index,n,m):
    if index==m:
        print(' '.join(map(str,result)))
        return
    else:
        for k in arr:
            if not visited[k]:
                visited[k]=True
                result.append(k)
                back_tracking(index+1,n,m)
                visited[k]=False
                result.pop()
back_tracking(0,n,m)
