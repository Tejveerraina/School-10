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
start=int(input("Enter starting number "))
end=int(input("Enter ending number "))
if start%2==0:
    for x in range(start,end,2):
        print(x,end=" ")
else:
    for x in range(start+1,Stop,2):
        print(x,end="")
    
        