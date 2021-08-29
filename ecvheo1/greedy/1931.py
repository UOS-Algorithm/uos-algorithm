import sys

n = int(input())
arr = []
for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

arr.sort(key = lambda x: (x[1], x[0]))

count = a = 0
for i, j in arr:
    if i >= a:
        a = j
        count += 1

print(count)