import sys

n,m = map(int,sys.stdin.readline().split())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

start = 0
end = 0
cnt = 2e9+1

while start < n and end < n:
    if arr[end] - arr[start] < m:
        end+=1
    elif arr[end] - arr[start] == m:
        print(m)
        exit()
    elif arr[end] - arr[start] > m:
        cnt = min(cnt,arr[end]-arr[start])
        start+=1
    
print(cnt)