import sys

case = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

sum = 0

for _ in range(case-1):
    arr.sort()
    arr.reverse()
    newVal = arr[0]*arr[1] 
    newSum = arr[0]+arr[1]
    sum+=newVal
    arr.append(newSum)
    arr.pop(0)
    arr.pop(0)

    


print(sum)