import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
d = [deque(), deque()]
ground = [deque(), deque()]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    d[0].append(a)
    d[1].append(b)

turn = 0 
for _ in range(m):
    ground[turn].append(d[turn].pop())
    win = -1
    if not d[turn]:
        break
    if ground[turn][-1] == 5:
        win = 0
    elif ground[0] and ground[1] and ground[turn][-1] + ground[1-turn][-1] == 5:
        win = 1
    if win != -1:
        for i in [1-win, win]:
            while ground[i]:
                d[win].appendleft(ground[i].popleft())
    turn = 1-turn

if len(d[0]) > len(d[1]):
    print('do')
elif len(d[0]) < len(d[1]):
    print('su')
else:
    print('dosu')