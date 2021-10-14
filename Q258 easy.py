num=int(input("enter the number"))
i=num
b=0
while num>0:
    a=num%10
    b=b+a
    num//=10
sum=0
while b>0:
    c=b%10
    sum=sum+c
    b=b//10
print(sum)

