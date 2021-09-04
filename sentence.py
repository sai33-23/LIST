sentence="myself sai and i'm from odisha"
a=sentence.split()
b=[]
i=0
while i<len(a):
    if a[i]==sentence:
        b.append(a[i])
    i=i+1
print(b)