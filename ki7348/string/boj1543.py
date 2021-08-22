import sys

x = sys.stdin.readline().strip()
y = sys.stdin.readline().strip()
arr=[]
arr.append(y)

count=0
for i in arr:
    for _ in x:
        if i in x:
            x=x.replace(i,' ',1)
            count+=1

print(count)


# word = input()
# target= input()

# print(word.count(target))