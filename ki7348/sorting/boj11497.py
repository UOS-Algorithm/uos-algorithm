import sys

case = int(sys.stdin.readline())

for _ in range(case):
    num = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))

    sorted_arr = sorted(arr, reverse=True)

    max_num = 0

    if sorted_arr[0] - sorted_arr[1] > max_num:
        max_num = sorted_arr[0]-sorted_arr[1]
    if sorted_arr[0] - sorted_arr[2] > max_num:
        max_num = sorted_arr[0]-sorted_arr[2]
    for i in range(1,len(sorted_arr)-2):
        if sorted_arr[i] -sorted_arr[i+2] > max_num:
            max_num = sorted_arr[i] -sorted_arr[i+2]

    print(max_num)