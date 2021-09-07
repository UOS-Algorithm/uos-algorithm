import sys

buffer = int(sys.stdin.readline())
queue = []
while True:
    x = int(sys.stdin.readline())
    if x == -1:
        if len(queue) == 0:
            print('empty')
            break
        else:
            print(' '.join(map(str,queue)))
        break
    if x > 0:
        if len(queue) < buffer:
            queue.append(x)
    elif x == 0:
        queue.pop(0)
    