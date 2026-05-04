#Wap to generate even numbers from given range of numbers
#Wap[ to generate odd numbers from given range of numbers
#wap to check wether the given number is prime or not


#method 1
"""""
Start=int(input("enter starting number: "))
End=int(input("enter ending number: "))
for x in range(Start,End):
    if x%2==0:
        print(x)"""
    
#method 2
"""
start=int(input("Enter starting number "))
end=int(input("Enter ending number "))
if start%2==0:
    for x in range(start,end,2):
        print(x,end=" ")
else:
    for x in range(start+1,Stop,2):
        print(x,end="")"""
    
"""
start=int(input("Enter starting number "))
end=int(input("Enter ending number "))
if start%2!=0:
    for x in range(start,end):
        print(x)
"""
#wap to check prime number
start=int(input("Enter number: "))
c=0
for x in range (1,start+1):
    c=c+1
    if c==2:
        print(start,"is a prime number")
    else:
        print(start,"is a composite")
#WAP to test the number entered armstrong or not
num=int(input("Enter number to be tested"))


