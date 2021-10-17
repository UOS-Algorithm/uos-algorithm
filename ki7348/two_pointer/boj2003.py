import sys


n,m = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

start = 0
end = 0
total = 0
count = 0


while start < n:
    if total == m:
        count += 1
        total -= arr[start]
        start += 1
    elif total > m or end >= n:
        total -= arr[start]
        start += 1
    elif total < m:
        total += arr[end]
        end+= 1

print(count)