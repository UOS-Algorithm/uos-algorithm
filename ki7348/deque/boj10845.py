import sys
from collections import deque

case = int(sys.stdin.readline())

queue = deque()
for i in range(case):
    desc = sys.stdin.readline().split()
    if desc[0] == 'push':
        queue.append(desc[1])
    elif desc[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif desc[0] == 'size':
        print(len(queue))
    elif desc[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif desc[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)