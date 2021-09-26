import sys

s = sys.stdin.readline().rstrip()
stack = []
result = 0

for i in s:
    if i == ')':
        v = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '(':
                if v == 0:
                    stack.append(2)
                else:
                    stack.append(2*v)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                v = v + int(top)
    elif i == ']':
        v = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '[':
                if v == 0:
                    stack.append(3)
                else:
                    stack.append(3*v)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                v = v + int(top)
    else:
        stack.append(i)

for i in stack:
    if i == '(' or  i == '[':
        print(0)
        exit(0)
    else:
        result += i

print(result)    