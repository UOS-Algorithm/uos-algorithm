import sys

n = int(sys.stdin.readline())

def is_good(x):
    if len(x) == 1:
        return True
    for i in range(1,len(x)//2+1):
        if x[-i:] == x[-2*i:-i]:
            return False
    return True


def back_tracking(x):
    if len(x) == n:
        print(x)
        exit()
    for i in range(1,4):
        x = x+str(i)
        if is_good(x):
            back_tracking(x)
        x = x[:-1]


back_tracking('')
