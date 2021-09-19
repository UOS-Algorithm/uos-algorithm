import sys

case = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
ans = [0] * case
stack = []

for i in range(case-1,-1,-1):
    if len(stack) == 0:
        stack.append([i, arr[i]])
    else:
        while arr[i] > stack[len(stack)-1][1]:
            ans[stack[len(stack)-1][0]] = i+1
            stack.pop()
            if len(stack) == 0:
                break
        stack.append([i,arr[i]])

print(' '.join(map(str,ans)))