import sys

num = 1

while True:
    x = sys.stdin.readline().strip()
    if '-' in x:
        break
    count = 0
    arr=[]

    for i in x:
        if i == '{':
            arr.append(i)
        elif i == '}':
            if len(arr)!=0 and arr[-1]=='{':
                arr.pop()
            else:
                count+=1
                arr.append('{')
        
    while arr:
        if len(arr)%2 == 0:
            count+=1
        arr.pop()


    print('{}. '.format(num)+str(count))
    num+=1