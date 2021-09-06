import sys

form = list(sys.stdin.readline().rstrip())

stack = []
result = 0

for i in range(len(form)):
    if form[i] == '(' and form[i+1] != ')':
        stack.append(form[i])
    elif form[i] == '(' and form[i+1] == ')':
        result+=len(stack)
    elif form[i] == ')' and form[i-1] != '(':
        if stack:
            stack.pop()
            result+=1

print(result)
