import sys

n, t = map(int,sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

result = 0
arr.sort(key=lambda x:x[1] )
cnt = 0
for i in arr:
    
    result += i[0]+i[1]*(t-n+cnt)
    cnt+=1

print(result)