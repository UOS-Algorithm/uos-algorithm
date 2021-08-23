# import sys

# a = sys.stdin.readline().strip()
# b = sys.stdin.readline().strip()

# while b in a:
#     a=a.replace(b,'')


# if a:
#     print(a)
# else:
#     print('FRULA')


import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

arr=[]

tick = len(b)

for i in a:
    arr.append(i)
    if b[-1] == i and ''.join(arr[-tick:]) == b:
        del arr[-tick:]

if arr:
    print(''.join(arr))
else:
    print('FRULA')
    