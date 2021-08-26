n, k = map(int, input().split())
a = list(int(input()) for _ in range(n))

count = 0

for i in range(n-1, -1, -1):
    if k == 0:
        break
    if a[i] <= k:
        count += k // a[i]
        k = k % a[i]

print(count)