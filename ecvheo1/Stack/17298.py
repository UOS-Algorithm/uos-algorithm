n = int(input())
a = list(map(int, input().split()))
stack = []
answer = []

for i in range(n-1, -1, -1):
    t = a[i]
    while stack and stack[-1] <= t:
        stack.pop()
    if stack:
        answer.append(stack[-1])
    else:
        answer.append(-1)
    stack.append(t)

print(' '.join(map(str, answer[::-1])))