
#WAP to find weather a no is prime or not
num=int(input("no."))
c=0
for x in range (1,num+1):
    if num%x==0:
        c=c+1
if c==2:
    print(num,"prime")
else:
    print(num,"not prime")

#WAP print all prime no from1 to100
for x in range (1,101):
    for i in range(2,x):
        if (x%i)==0:
            break
    else:
        print(x,end="")



    
    
