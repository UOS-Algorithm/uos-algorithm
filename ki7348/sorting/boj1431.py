import sys

arr = []

case = int(sys.stdin.readline())

for _ in range(case):
    a = sys.stdin.readline().strip()
    sum = 0
    for i in a:
        if 48<=ord(i)<=57:
            sum+=int(i)
    arr.append((a,sum))

arr.sort(key=lambda x: (len(x[0]),x[1],x))

for i in arr:
    print(i[0])