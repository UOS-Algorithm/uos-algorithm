from collections import deque

n = int(input())
li = []
for i in range(n, 0, -1):
    li.append(i);

cardDeque = deque(li)

while len(cardDeque) != 1:
    cardDeque.pop()
    cardDeque.appendleft(cardDeque.pop())

print(cardDeque[0])