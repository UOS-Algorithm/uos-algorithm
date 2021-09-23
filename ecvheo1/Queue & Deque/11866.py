from collections import deque

n, k = map(int, input().split())
one = []
answer = []
i = 0

for i in range(1, n+1):
    one.append(str(i))
oneDeque = deque(one)

while oneDeque:
    for _ in range(k-1):
        oneDeque.append(oneDeque.popleft())
    answer.append(oneDeque.popleft())

print(f"<{', '.join(answer)}>")