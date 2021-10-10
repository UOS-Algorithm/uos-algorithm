import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
diff = []
for i in range(n-1):
    diff.append(arr[i+1]-arr[i])

diff.sort()


if k>n:
    print(0)
else:
    for i in range(k-1):
        diff.pop()
    print(sum(diff))