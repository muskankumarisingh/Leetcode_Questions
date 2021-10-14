list=[2,7,11,15]
num=int(input("enter your target:"))
a=[]
i=0
while i<len(list):
    j=i
    while j<len(list):
        b=list[i]+list[j]
        if b==num:
            a.append(i)
            a.append(j)
        j=j+1
    i=i+1
print(a)

#[0,1]