import sys

x = sys.stdin.readline().strip()

stack = []
count = 0

for i in x:
    if i == '(':
        stack.append(i)
    elif i == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            count+=1

if stack:
    count+=len(stack)

print(count)