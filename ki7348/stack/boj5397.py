import sys

case = int(sys.stdin.readline())

for i in range(case):
    lstack=[]
    rstack=[]
    x = sys.stdin.readline().strip()
    for i in x:
        if i != '-' and i != '<' and i != '>':
            lstack.append(i)
        elif i == '-':
            if lstack:
                lstack.pop()
        elif i == '<':
            if lstack:
                rstack.append(lstack.pop())
        elif i ==  '>':
            if rstack:
                lstack.append(rstack.pop())

    while rstack:
        lstack.append(rstack.pop())
    print(''.join(lstack))