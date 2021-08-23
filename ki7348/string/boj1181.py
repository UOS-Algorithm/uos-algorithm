import sys

case = int(sys.stdin.readline().strip())
arr=[]

for i in range(case):
    arr.append(sys.stdin.readline().strip())

arr=list(set(arr))

arr.sort(key=lambda x:(len(x),x))


for i in arr:
    print(i)