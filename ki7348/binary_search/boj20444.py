import sys

n, k = map(int,sys.stdin.readline().split())

start = 0
end = n // 2

while start <= end:
    mid = (start  + end )//2

    value = (mid+1)*(n-mid+1)

    if value > k:
        end = mid - 1
    elif value < k:
        start = mid  + 1
    else:
        print('YES')
        exit()

print('NO')