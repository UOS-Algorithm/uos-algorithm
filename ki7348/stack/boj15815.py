import sys

x = sys.stdin.readline().strip()

result = 0

stack = []

for i in x:
    if i == '+':
        a=stack.pop()
        b=stack.pop()
        stack.append(a+b)
    elif i == '*':
        a=stack.pop()
        b=stack.pop()
        stack.append(a*b)
    elif i == '-':
        a=stack.pop()
        b=stack.pop()
        stack.append(b-a)
    elif i == '/':
        a=stack.pop()
        b=stack.pop()
        stack.append(b//a)
    else:
        stack.append(int(i))

for j in stack:
    print(j)