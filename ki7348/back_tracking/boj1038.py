import sys

n = int(sys.stdin.readline())

if n > 1022:
    print(-1)
    exit()
arr = []

def back_tracking(x):
    arr.append(int(x))
    for i in range(0,int(x[-1])):
        back_tracking(x+str(i))


for i in range(0,10):
    back_tracking(str(i))

arr.sort()
print(arr[n])