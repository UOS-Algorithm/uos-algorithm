import sys

k = int(sys.stdin.readline())
visited = [False]*10

arr = list(sys.stdin.readline().split())

def bigger_or_smaller(i,j,k):
    if k == '>':
        return i > j
    elif k == '<':
        return i < j
store = []
def back_tracking(cnt,n):

    if len(n) == k+1:
        store.append(n)
        return
    else:
        for i in range(10):
            if not visited[i] and (cnt == 0 or bigger_or_smaller(n[-1],str(i),arr[cnt-1])):
                visited[i] = True
                back_tracking(cnt+1,n+str(i))
                visited[i] = False


back_tracking(0,'')
print(store[-1])
print(store[0])