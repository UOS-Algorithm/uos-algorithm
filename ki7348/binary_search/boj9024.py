import sys

case = int(sys.stdin.readline())

for _ in range(case):
    n,k = map(int,sys.stdin.readline().split())

    arr = list(map(int,sys.stdin.readline().split()))

    arr.sort()

    start = 0
    end = n-1


    min_diff = max(abs(max(arr)-k),abs(min(arr)-k))
    count = 1
    while start<end:

        total = arr[start] + arr[end]
        if abs(total-k) < min_diff:
            min_diff = abs(total-k)
            count = 1    
        elif abs(total-k) == min_diff:
            count+=1


        if total <= k:
            start += 1
        elif total > k:
            end-=1
    print(count)
