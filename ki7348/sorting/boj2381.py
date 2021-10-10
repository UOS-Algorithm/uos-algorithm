import sys

case = int(sys.stdin.readline())
arr = []
arr2 = []
for _ in range(case):
    a, b = map(int,sys.stdin.readline().split())
    arr.append([a,b,a-b])
    arr2.append([a,b,a+b])
arr.sort(key=lambda x:(x[2]))
arr2.sort(key=lambda x:x[2])


print(max((arr[-1][2]-arr[0][2]),arr2[-1][2]-arr2[0][2]))

