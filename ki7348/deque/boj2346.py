import sys
from collections import deque

case = int(sys.stdin.readline())
queue = deque(enumerate(map(int,sys.stdin.readline().split())))

result = []

while queue:
    idx, num = queue.popleft()
    result.append(idx+1)

    if num > 0:
        queue.rotate(-(num-1))
    else:
        queue.rotate(-num)
    
print(*result)