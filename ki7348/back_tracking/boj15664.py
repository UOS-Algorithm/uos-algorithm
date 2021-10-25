import sys

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
result = []
visited = [False]*(n)

def back_tracking(index,idx,n,m):
    temp = 0
    if index==m:
        print(*result)
        return
    else:
        for k in range(idx,n):
            if not visited[k] and temp != arr[k]:
                visited[k] = True
                result.append(arr[k])
                temp = arr[k]
                back_tracking(index+1,k+1,n,m)
                visited[k] = False
                result.pop()
back_tracking(0,0,n,m)
