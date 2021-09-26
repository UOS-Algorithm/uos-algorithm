import sys
from collections import deque

n = int(sys.stdin.readline())
a =  list(map(int, sys.stdin.readline().split()))
card = list(i for i in range(n, 0, -1))
result = deque(list())

for i in a[-1::-1]:
    if i == 1:
        result.appendleft(card.pop())
    else:
        if i == 2:
            result.insert(1, card.pop())
        if i == 3:
            result.append(card.pop())
            
print(*result)