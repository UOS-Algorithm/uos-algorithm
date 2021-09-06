stick = input()
stickStack = []
answer = 0
for i in range(len(stick)):
    if stick[i] == '(':
        stickStack.append('(')
    else:
        if stick[i-1] == '(':
            stickStack.pop()
            answer += len(stickStack)
        else:
            stickStack.pop()
            answer += 1
print(answer)