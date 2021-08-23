import sys

case = int(sys.stdin.readline())
arr=[]
for i in range(case):
    x,y = map(str,sys.stdin.readline().split())
    if y == 'enter':
        arr.append(x)
    else: 
        arr.remove(x)

arr.sort()
arr.reverse()

for i in arr:
    print(i)