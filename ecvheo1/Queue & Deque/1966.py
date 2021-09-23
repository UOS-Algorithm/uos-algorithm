from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    statusDeque = deque(list(map(int, input().split())))
    k = statusDeque[m]
    count = 0
    maxValue = max(statusDeque)
    while k != maxValue or m != 0:
        if statusDeque[0] != maxValue:
            statusDeque.append(statusDeque.popleft())
        else:
            statusDeque.popleft()
            maxValue = max(statusDeque)
            count += 1
            n -= 1
        if m == 0:
            m = n-1
        else:
            m -= 1
    count += 1
    print(count)