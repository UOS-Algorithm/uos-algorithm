# import sys

# case = int(sys.stdin.readline())
# arr=[]
# for _ in range(case):
#     data=sys.stdin.readline().split()
#     arr.append((int(data[0]),int(data[1])))

# sum = 0

# for i in range(case-1):
#     if arr[i][0] < arr[i+1][0] and arr[i][1] > arr[i+1][1]:
#         arr.pop(i+1)


# sum+=arr[len(arr)-1][1]-arr[0][0]

# if len(arr) > 1:
#     for i in range(case-1):
#         if arr[i+1][0] > arr[i][1]:
#             sum-=arr[i+1][0] - arr[i][1]




# print(sum)


import sys

case = int(sys.stdin.readline())
arr=[]

n,m=map(int,sys.stdin.readline().split())

result = 0
for i in range(case-1):
    newn, newm=map(int,sys.stdin.readline().split())
    if newn == n:
        m = newm
    elif m >= newn and newm > m:
        m = newm
    elif newn > m:
        result += (newn - m)
        m = newm
        


print(m-n-result)

