import sys

n = int(sys.stdin.readline())

sang = list(map(int,sys.stdin.readline().split()))
sang.sort()

m = int(sys.stdin.readline())

card = list(map(int,sys.stdin.readline().split()))

def binary_search(x):
    start = 0
    end = n-1

    while start<=end:
        mid = (start+end) // 2
        
        if x<sang[mid]:
            end = mid-1
        elif x>sang[mid]:
            start = mid+1
        else:
            return True
    return False
    
result = []
for i in card:
    k = binary_search(i)
    if k == True:
        result.append(1)
    else:
        result.append(0)

print(*result)