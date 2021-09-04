numbers=[1,6,9,4,67,53 ,79]
i=0
max=numbers[0]
while i<len(numbers):
    if numbers[i]<max:
        max=numbers[i]
    i=i+1
print(max)