import sys

n,s = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
visited = [False] * n
cnt = 0
print('최시열')
def back_tracking(x,first):
    global cnt
    if x == s and first != 0:
        cnt+=1
        return
    for i in range(n):
        if not visited[i]:
            x+=arr[i]
            visited[i] = True
            first+=1
            back_tracking(x,first)
            first-=1
            visited[i] = False
            x-=arr[i]

back_tracking(0,0)
print(cnt)