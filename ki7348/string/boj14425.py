# import sys

# n,m = map(int,sys.stdin.readline().split())

# arr=[]
# count=0
# for _ in range(n):
#     arr.append(sys.stdin.readline())

# for _ in range(m):
#     x = sys.stdin.readline()
#     if x in arr:
#         count+=1


# print(count)


import sys
n, m = map(int,sys.stdin.readline().split())

narr=[]
marr=[]
count = 0
for _ in range(n):
    narr.append(sys.stdin.readline().strip())

narr.sort()

for _ in range(m):
    marr.append(sys.stdin.readline().strip())

marr.sort()

nindex = 0
mindex = 0

while nindex < n and mindex < m:
    if narr[nindex] == marr[mindex]:
        count+=1
        mindex+=1
    elif narr[nindex] > marr[mindex]:
        mindex+=1
    else:
        nindex+=1

print(count)