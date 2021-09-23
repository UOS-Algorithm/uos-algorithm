n = int(input())
idx = 0

data = list(map(int, input().split()))
index = [x for x in range(1, n + 1)]

temp = data.pop(idx)
print(index.pop(idx), end=" ")

while data:
    if temp < 0:
        idx = (idx + temp) % len(data)
    else:
        idx = (idx + (temp - 1)) % len(data)
    temp = data.pop(idx)
    print(index.pop(idx), end=" ")