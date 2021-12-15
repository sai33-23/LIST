n=int(input("enter a number"))
a=[]
b=[]
c=[]
sum=0
i=0
while i<n:
    n1=int(input("enter the number"))
    a.append(n1)
    n2=int(input("enter the  2nd number"))
    b.append(n2)
    i=i+1
j=0
while j<len(a):
    sum=a[j]+b[j]
    c.append(sum)
    j=j+1
print(c)
    
