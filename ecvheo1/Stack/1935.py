n = int(input())
li = list(input())
nums = [int(input()) for _ in range(n)]
stack = []
for t in li:
    if t in "+-*/":
        a = stack.pop()
        b = stack.pop()
        if t == '+':
            stack.append(b+a)
        elif t == '-':
            stack.append(b-a)
        elif t == '*':
            stack.append(b*a)
        elif t == '/':
            stack.append(b/a)
    else:
        stack.append(nums[ord(t)-ord('A')])
print("%.2f" % (stack[0]))