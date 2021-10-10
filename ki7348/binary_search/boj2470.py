import sys


n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

start = 0
end = n-1
initial_start = arr[start]
initial_end = arr[end]

while start < end:
    total = arr[start] + arr[end]
    if abs(initial_start + initial_end) >= abs(total):
        initial_start = arr[start]
        initial_end = arr[end]
    if total == 0:
        print(arr[start], arr[end])
        exit()
    elif total < 0:
        start += 1
    elif total > 0:
        end-=1


print(initial_start, initial_end)