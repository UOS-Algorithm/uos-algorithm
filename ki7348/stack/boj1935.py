import sys

case = int(sys.stdin.readline())

form = sys.stdin.readline().strip()
num = []
for i in range(case):
    num.append(int(sys.stdin.readline()))
stack = []
for i in form:
    if i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
    elif i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    else:
        if i.isupper():
            stack.append(num[ord(i)-ord('A')])

for j in stack:
    print("{:.2f}".format(j))