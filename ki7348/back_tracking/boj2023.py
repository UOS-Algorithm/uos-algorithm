import sys
import math

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True 

n = int(sys.stdin.readline())
result = []
def back_tracking(k):
    if len(k) == n:
        result.append(k)
        return
    else:
        for i in range(1,10):
            k = k+str(i)
            if is_prime(int(k)):
                back_tracking(k)
            k = k[:-1]



    

back_tracking('')
for i in result:
    print(i)