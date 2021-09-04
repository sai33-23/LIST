l1=[1,2,3,4,5,6,7]
l2=[2,3,9,0,6,5,3]
i=0
k=[]
while i<len(l1):
    j=0
    while j<len(l2):
        if l1[i] not in l2[j]:
            k.append(l1)
            j=j+1
    i=i+1
print(j)
