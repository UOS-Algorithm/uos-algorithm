import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    arr = []
    for _ in range(n):
        arr.append(int(sys.stdin.readline()))
    
    d = [0] * n
    d[0] = arr[0]

    for  i in range(1,n):
        d[i] = max(arr[i],d[i-1] + arr[i])

    print(max(d))