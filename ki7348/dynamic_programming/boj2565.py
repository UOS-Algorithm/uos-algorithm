import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort(key=lambda x:x[0])


d = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i][1] >= arr[j][1]:
            d[i] = max(d[j]+1,d[i])

print(n-max(d))