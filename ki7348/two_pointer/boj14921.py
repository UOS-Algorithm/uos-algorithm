import sys


n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

start = 0
end = n-1
min_diff = (max(arr)+min(arr))


while start < end:
    total = arr[start] + arr[end]
    if abs(total) < abs(min_diff):
        min_diff = (total)

    if total <= 0:
        start += 1
    elif total > 0:
        end-=1


print(min_diff)