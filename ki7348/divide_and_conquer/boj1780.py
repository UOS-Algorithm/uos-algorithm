import sys

n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

one = 0
minus_one = 0
zero = 0

def divide(x,y,n):
    global one,minus_one,zero
    check=arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=arr[i][j]:
                temp = n//3
                divide(x,y,temp)
                divide(x+temp,y,temp)
                divide(x+2*temp,y,temp)
                divide(x,y+temp,temp)
                divide(x,y+2*temp,temp)
                divide(x+temp,y+temp,temp)
                divide(x+2*temp,y+temp,temp)
                divide(x+temp,y+2*temp,temp)
                divide(x+2*temp,y+2*temp,temp)
                return

 
    if check==0:
        zero+=1
        return
    elif check == 1:
        one+=1
        return
    else:
        minus_one+=1
        return
 
 
divide(0,0,n)
print(minus_one)
print(zero)
print(one)