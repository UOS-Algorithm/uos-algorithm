import sys

n,s = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

end = 0
interval_sum = 0
length = n
cnt = 0

for start in range(n):
    while interval_sum<s and end<n:
        interval_sum+=arr[end]
        end+=1
    if interval_sum >= s:
        if end - start <= length:
            length = end-start
            cnt+=1
    interval_sum -= arr[start]

if cnt == 0:
    print(0)
else:
    print(length)
