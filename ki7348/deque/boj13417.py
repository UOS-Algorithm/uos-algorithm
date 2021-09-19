import sys

case = int(sys.stdin.readline())

for _ in range(case):
    x = int(sys.stdin.readline())
    queue= list(map(str,sys.stdin.readline().split()))
    arr = [queue[0]]

    for i in range(1,x):
        if queue[i] <= arr[0]:
            arr.insert(0, queue[i])
        else:
            arr.append(queue[i])
    
    print(''.join(arr))