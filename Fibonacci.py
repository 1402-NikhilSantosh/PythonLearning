a=0
b=1
c=0
n=int(input("Enter nth number: "))
while c<=n:
    print(a)
    d=a+b
    a=b
    b=d
    c+=1
    
