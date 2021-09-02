import sys

def push(k):
    stack.append(k)

def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def top():
    return stack[-1] if stack else -1


n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    x = sys.stdin.readline().rstrip().split()
    order = x[0]

    if order == 'push':
        push(x[1])
    elif order == 'pop':
        print(pop())
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    elif order == 'top':
        print(top())
