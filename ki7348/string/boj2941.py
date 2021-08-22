import sys

arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']

x = sys.stdin.readline().strip()

count = 0

for i in arr:
    if i in x:
        x=x.replace(i,' ')

        
print(len(x))