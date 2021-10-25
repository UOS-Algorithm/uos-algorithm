import sys

n,k = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

start = 0
end = 0
temp = [0]*100001
result = 0

while end < n:
    if temp[arr[end]] != k:
        temp[arr[end]] += 1
        end += 1
    else:
        temp[arr[start]] -= 1
        start += 1
    result = max(result,end-start)

print(result)