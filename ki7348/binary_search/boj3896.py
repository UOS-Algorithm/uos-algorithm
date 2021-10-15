import sys
import math

case = int(sys.stdin.readline())

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for _  in range(case):
    k = int(sys.stdin.readline())
    if isPrime(k):
        print(0)
        
    else:
        start = 0
        end = 1299709

        while start <= end:
            mid = (start+end) // 2
            total = 1

            for i in range(1,min(k,mid)):
                if not isPrime(k - i):
                    total += 1
                else:
                    break

            for i in range(1,min(k,mid)):
                if not isPrime(k + i):
                    total += 1
                else:
                    break
            
            if total < mid:
                end = mid - 1
            else:
                start = mid + 1
        print(start)