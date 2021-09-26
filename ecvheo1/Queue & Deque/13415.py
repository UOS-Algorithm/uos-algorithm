import sys
from collections import deque

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

setDeque = deque()

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    while setDeque and abs(setDeque[len(setDeque)-1]) <= a:
        setDeque.pop()
    setDeque.append(a)
    while setDeque and abs(setDeque[len(setDeque)-1]) <= b:
        setDeque.pop()
    setDeque.append(-b)

answer = deque()
setDeque.append(0)
j = abs(setDeque[0])
x = deque(sorted(li[0:j]))

for _ in range(len(setDeque)-1):
    i = setDeque.popleft()
    if i > 0:
        for _ in range(abs(i)-abs(setDeque[0])):
            answer.appendleft(x.pop())
    else:
        for _ in range(abs(i)-abs(setDeque[0])):
            answer.appendleft(x.popleft())

answer.extend(li[j:])
print(*answer)