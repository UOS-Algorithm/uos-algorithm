import sys

n = int(sys.stdin.readline())

graph = [[' ' for _ in range(n)] for _ in range(n)]

def divide(x,y,n):
    if n == 1:
        graph[y][x] = '*'
    else:
        temp = n//3
        for j in range(3):
            for i in range(3):
                if i != 1 or j != 1:
                    divide(x+i*temp, y+j*temp, temp)
    
divide(0,0,n)

for i in graph:
    print(''.join(i))