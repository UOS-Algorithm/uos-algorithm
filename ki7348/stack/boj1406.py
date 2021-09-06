import sys

lstack = list(map(str,sys.stdin.readline().strip()))
rstack = []

case = int(sys.stdin.readline())


for i in range(case):
    edit = sys.stdin.readline().split()
    if edit[0] == 'P':
        lstack.append(edit[1])
    elif edit[0] == 'L':
        if lstack:
            rstack.append(lstack.pop())
    elif edit[0] == 'D':
        if rstack:
            lstack.append(rstack.pop())
    elif edit[0] == 'B':
        if lstack:
            lstack.pop()


rstack.reverse()
print(''.join(lstack+rstack))

