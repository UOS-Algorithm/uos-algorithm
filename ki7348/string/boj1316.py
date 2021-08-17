import sys

case = int(sys.stdin.readline())

count = 0
for i in range(case):
    x = sys.stdin.readline().strip()
    no=0
    for j in range(len(x)-1):
        if x[j] != x[j+1]:
            newx=x[j+1:]
            if newx.find(x[j]) > 0:
                no+=1
    if no == 0:
        count+=1


print(count)