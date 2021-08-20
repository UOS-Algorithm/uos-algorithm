import sys

s = sys.stdin.readline().strip()
x = list(sys.stdin.readline().strip())

answer = []

for i in s:
    answer.append(i)
    if i == x[-1]:
        if answer[-1:-len(x)-1:-1] == x[-1:-len(x)-1:-1]:
            for _ in range(len(x)):
                answer.pop()

if len(answer) == 0:
    print("FRULA")
else:
    print("".join(answer))