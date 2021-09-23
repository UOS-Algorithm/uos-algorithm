import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
i = b.index(a[0])
flag = False

if n < 4:
    flag = True
else:
    if i == 0:
        if a[1:] == b[1:] or a[1:] == b[-1:0:-1]:
            flag = True
    elif i == n-1:
        if a[1:] == b[:-1] or a[1:] == b[-2::-1]:
            flag = True
    else:
        if (a[1:i+1] == b[i-1::-1] and a[i+1:] == b[:i:-1]) or (a[1:n-i] == b[i+1:] and a[n-i:] == b[:i]):
            flag = True

if flag: print('good puzzle')
else: print('bad puzzle')