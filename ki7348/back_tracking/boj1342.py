import sys

dict = {'a': 0, 
'b': 0, 
'c': 0, 
'd': 0, 
'e': 0, 
'f': 0, 
'g': 0, 
'h': 0, 
'i': 0, 
'j': 0, 
'k': 0, 
'l': 0, 
'm': 0, 
'n': 0, 
'o': 0, 
'p': 0, 
'q': 0, 
'r': 0, 
's': 0, 
't': 0,
'u': 0, 
'v': 0, 
'w': 0, 
'x': 0,
'y': 0, 
'z': 0, }

string = sys.stdin.readline().strip()

for i in string:
    dict[i] += 1
count = 0
def back_tracking(x):
    global count
    if len(x) == len(string):
        count+=1
        return
    for i in dict:
        if dict[i] > 0:
            if len(x) == 0:
                x = x+i
                dict[i]-=1
                back_tracking(x)
                x=x[:-1]
                dict[i]+=1
            else:
                if x[-1] != i:
                    x = x+i
                    dict[i]-=1
                    back_tracking(x)
                    x=x[:-1]
                    dict[i]+=1



back_tracking('')
print(count)