#wap to calculate the electricity bill 
a=int(input( "Total units"))
if a>0 and a<=100:
    bill=a*5
elif a>100 and a<=200:
    bill= 500+((a-100)*7)
elif a>200 and a<=300:
    bill= 1200 + ((a-200)*10)
else:
    print("Invalid input")
if bill > 2000:
    bill= bill * 1.05
elif a<50:
    bill= bill -100

print("the total bill is ",bill)




    
    
