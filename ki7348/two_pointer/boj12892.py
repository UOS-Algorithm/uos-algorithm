import sys


n,d = map(int,sys.stdin.readline().split())

arr = []

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort(key=lambda x:x[0])

start = 0
end = 0
total = 0
result = 0


while start < n and end < n:
    if arr[end][0] - arr[start][0] < d:
        total += arr[end][1]
        end += 1
    else:
        total -= arr[start][1]
        start += 1
    result = max(result,total)

print(result)