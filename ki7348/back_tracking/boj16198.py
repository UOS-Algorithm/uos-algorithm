import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

max_val = 0

def back_tracking(temp_sum):
    global max_val
    if len(arr) == 2:
        max_val = max(max_val,temp_sum)
        return 
    else:
        for i in range(1,len(arr)-1):
            total = arr[i-1] * arr[i+1]
            temp = arr[i]
            del arr[i]
            back_tracking(temp_sum + total)
            arr.insert(i,temp)


back_tracking(0)
print(max_val)