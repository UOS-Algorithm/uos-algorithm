import sys

case = int(sys.stdin.readline())
arr = []

for _ in range(case):
    n,m = map(int,sys.stdin.readline().split())
    arr.append((n,m))

arr.sort(key=lambda x:(x[0],x[1]))
result = 0
cur = arr[0][0]
end = arr[0][1]
for i in range(len(arr)-1): #0 1 2
    if end < arr[i+1][0]:
        result+=end-cur
        cur = arr[i+1][0]
        end = arr[i+1][1]
    if end >= arr[i+1][0]:
        if end < arr[i+1][1]:
            end = arr[i+1][1]

result+=end-cur

print(result)