import sys

n, m = map(int,sys.stdin.readline().split())

count=1


while True:
    if m == n:
        print(count)
        break
    if ( m % 2 != 0 and m %10 != 1)  or m < n:
        print(-1) 
        break
    if m % 10 == 1:
        m=m//10
        count+=1
    else:
        m=m//2
        count+=1
