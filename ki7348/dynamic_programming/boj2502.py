import sys

a,b = map(int,sys.stdin.readline().split())

d = [0]*(a+1)

d[1] = 1
d[2] = 1

while True:
    for i in range(3,a+1):
        d[i] = d[i-1] + d[i-2]
    
    if d[a] == b:
        break
    elif d[a] < b:
        d[2] += 1
    elif d[a] > b:
        d[2] -= 1
        d[1] += 1


print(d[1])
print(d[2])