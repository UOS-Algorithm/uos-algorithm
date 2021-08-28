import sys

case = int(sys.stdin.readline())

tree = list(map(int,sys.stdin.readline().split()))
grow = list(map(int,sys.stdin.readline().split()))

arr=[]
for i in range(case):
    arr.append((tree[i],grow[i]))

arr.sort(key=lambda x:(x[1]))
sum=0
for i in range(case):
    sum+=arr[i][0]+arr[i][1]*i

print(sum)