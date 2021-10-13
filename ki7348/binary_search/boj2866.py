import sys
import copy
r,c = map(int,sys.stdin.readline().split())

arr = []
for _ in range(r):
    arr.append(list(sys.stdin.readline().strip()))

start = 0
end = r-1

while start <= end:
    mid = (start+end)//2
    total = 0
    mp = arr
    mp_arr = []


    for j in range(0,c):
        temp = ''
        for i in range(mid,len(mp)):
            temp+=mp[i][j]
        mp_arr.append(temp)

    if len(set(mp_arr)) != len(mp_arr):
        end = mid - 1
    else:
        start = mid + 1


print(start-1)
