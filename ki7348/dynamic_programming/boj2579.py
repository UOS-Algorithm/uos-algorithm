import sys

case = int(sys.stdin.readline())

arr = [0]*301

for i in range(case):
    x = int(sys.stdin.readline())
    arr[i] = x

d = [0]*301

d[0] = arr[0]
d[1] = arr[0] + arr[1] 
d[2] = max(arr[0]+arr[2], arr[1]+arr[2])

for i in range(3,case):
    d[i] = max(d[i-3]+arr[i-1]+arr[i],d[i-2]+arr[i])

print(d[case-1])