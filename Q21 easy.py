l1=[1,2,4]
l2=[1,3,4]
i=0
while i<len(l2):
    l1.append(l2[i])
    i=i+1
b=0
c=0
while c<len(l1):
    j=0
    while j<len(l1):
        if l1[c]<l1[j]:
            b=l1[j]
            l1[j]=l1[c]
            l1[c]=b
        j=j+1
    c=c+1
print(l1)


#[1,1,2,3,4,4]