import sys
n=int(sys.stdin.readline())
 
arr=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

result = []
def divide(x,y,n):
    check=arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=arr[i][j]:
                result.append('(')
                divide(x,y,n//2)
                divide(x,y+n//2,n//2)
                divide(x+n//2,y,n//2)
                divide(x+n//2,y+n//2,n//2)
                result.append(')')
                return

 
    if check==0:
        result.append(0)
        return
    else:
        result.append(1)
        return
 
 
divide(0,0,n)
print(''.join(map(str,result)))
