import sys

n,k = map(int,sys.stdin.readline().split())
cnt = 0

def back_tracking(sum_num,temp):
    global cnt
    if sum_num > n:
        return
    if n == sum_num:
        cnt+=1
        if cnt == k:
            a = (''.join(temp))
            print(a[:-1])
            exit()
    else:
        for i in range(1,4):
            temp.append(str(i)+'+')
            back_tracking(sum_num+i,temp)
            temp.pop()




back_tracking(0,[])
print(-1)