import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

spot = deque()
weight = deque()
wait = deque()
use = [0] * n
total = 0

for i in range(n):
    spot.append(int(sys.stdin.readline().strip()))
for i in range(m):
    weight.append(int(sys.stdin.readline().strip()))   
for i in range(m*2):
    car = int(sys.stdin.readline().strip())
    if car > 0:
        if 0 in use:
            for j in range(n):
                if use[j] == 0:
                    use[j] = car
                    break
        else:
            wait.append(car)
    else:
        a = use.index(-car)
        use[a] = 0
        total+=weight[-car-1]*spot[a]
        if wait:
            use[a] = wait.popleft()



print(total)