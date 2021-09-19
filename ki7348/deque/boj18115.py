import sys
from collections import deque

case = int(sys.stdin.readline())

queue = deque(map(int,sys.stdin.readline().split()))
queue.reverse()
index = 1
result = deque()


for i in queue: 
    if i == 1:
        result.appendleft(index)
    elif i == 2:
        temp = result.popleft()
        result.appendleft(index)
        result.appendleft(temp)
    else:
        result.append(index)

    index+=1
            

print(*result)