binary_number=[1,0,0,1,1,0,1,1]
i=-1
a=[]
while i>=-len(binary_number):
    a.append(binary_number[i])
    i-=1
j=0
sum=0
while j<len(a):
    sum=sum+2**j*a[j]
    j+=1
print(sum)
    