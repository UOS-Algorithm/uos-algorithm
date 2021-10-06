import sys

n, k = map(int,sys.stdin.readline().split())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))


diff = []
for i in range(len(arr)-1):
    diff.append(arr[i+1]-arr[i])

diff.sort()

for _ in range(k-1):
    diff.pop()

for _ in range(k):
    diff.append(1)
print(sum(diff))