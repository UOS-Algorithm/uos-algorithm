import sys
import math

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True 

n,m = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
visited = [False] * n
cnt = 0
result = []

def back_tracking(x):
    global cnt
    if cnt == m:
        if is_prime(x):
            result.append(x)
        return
    for i in range(n):
        if not visited[i]:
                x+=arr[i]
                visited[i] = True
                cnt+=1
                back_tracking(x)
                cnt-=1
                x-=arr[i]
                visited[i] = False

back_tracking(0)
if result:
    set_result = list(set(result))
    set_result.sort()
    print(*set_result)
else:
    print(-1)