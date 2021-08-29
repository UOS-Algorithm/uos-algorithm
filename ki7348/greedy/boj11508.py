import sys

case = int(sys.stdin.readline())

arr=[]

for _ in range(case):
    arr.append(int(sys.stdin.readline()))

sum = 0
arr.sort()
arr.reverse()

if len(arr)%3 == 1:
    arr.append(0)
    arr.append(0)
elif len(arr)%3 ==2:
    arr.append(0)
else:
    arr=arr

for i in range(len(arr)//3):
    sum+=arr[i*3+1]
    sum+=arr[i*3]

print(sum)
