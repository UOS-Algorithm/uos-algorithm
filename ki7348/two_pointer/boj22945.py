import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

start = 0
end = n-1

min_val = 0

while start <= end:
    min_val = max(min_val, (end-start-1)*min(arr[start],arr[end]))
    if arr[start] < arr[end]:
        start += 1
    else:
        end -= 1




print(min_val)
