number=30
n=[10,11,12,13,14,17,18,19]
i=0
new=[]
while i<len(n):
    j=0
    while j<len(n)//2:
        if n[i]+n[j]==number:
            k=[n[i],n[j]]
            new.append(k)
        j=j+1
    i=i+1
print(new)