# import sys

# case = int(sys.stdin.readline())

# for _ in range(case):
#     test = int(sys.stdin.readline())
#     ans=0
#     arr=list(map(int,sys.stdin.readline().split()))
#     for i in range(test-1):
#         if arr[i] < max(arr[i:]):
#             ans+=max(arr[i:])-arr[i]
#     print(ans)
            

import sys

case = int(sys.stdin.readline())

for _ in range(case):
    test = int(sys.stdin.readline())
    ans=0
    maxVal = 0
    arr=list(map(int,sys.stdin.readline().split()))
    for i in range(test-1,-1,-1):
        if arr[i] > maxVal:
            maxVal = arr[i]
        else:
            ans += maxVal - arr[i]
    print(ans)