import sys

g = int(sys.stdin.readline())

n = 0
for i in range(1,100000):
    if i**2 - (i-1)**2 >= g:
        n = i
        break

arr = []
for i in range(1,n+1):
    arr.append(i)

start = 0
end = 0
count = 0

while start < n and end < n:
    total = (arr[end])**2 - (arr[start])**2
    if total == g:
        print(end+1)
        count+=1
        start += 1
    elif total > g or end >= n:
        start += 1
    elif total < g:
        end+= 1

if count == 0:
    print(-1)