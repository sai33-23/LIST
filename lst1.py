n=int(input("enter number"))
i=0
a=[]
b=[]
c=[]
while i<n:
    n1=int(input("enter a number"))
    a.append(n1)
    i=i+1
    print(a)
    j=0
    while j<len(a):
        if a[j]%2==0:
            b.append(a[j])
        else:
            c.append(a[j])
        j=j+1
print(b,all even )
print(c,all odd )