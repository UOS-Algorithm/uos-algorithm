import sys

n, m = map(str,sys.stdin.readline().split())

count = 0
if len(n) != len(m):
    print(0)
else:
    if n[0] != m[0]:
        print(0)
    else:
        if n[0] == m[0] == '8':
            count+=1
        for i in range(1,len(n)):
            if n[i]!=m[i]:
                break
            else:
                if n[i] == m[i] == '8':
                    count+=1
        print(count)