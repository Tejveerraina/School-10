#wap a program to check the greater one number
#a=int(input("enter number_1:"))
#b=int(input("enter number_2:"))
#if a>b:
 #   print("number 1 is greater then number 2")
#if b>a:
    #print("number 2 is greater than number 1")
#if a==b:
    #print("the numbers are equal")

#wap to find the largest of three numbers

"""a=int(input("enter number 1 "))
b=int(input("enter number 2 "))
c=int(input("enter number 3 "))
if a==b and a==c:
    print("all are equal")
elif a>=b and a>=c:
    print(f"{a} is the largest")
elif b >=a and b>=c:
    print(f"{b} is the largest")
else:
    print(f"{c}is the largest")
"""
#WAP to check the posibility of triangle formation and if triangle is formed with the given three sides then identify the types of triangle
"""a=float(input("enter length of side 1"))
b=float(input("enter length of side 2"))
c=float(input("enter length of side 3"))
if a+b>c:
    print("this triangle is ")"""



#Basic Menu: Create a loop that displays a menu
#  (1: Add, 2: Exit)
#  and uses conditional statements to respond to user input,
#  repeating until the user selects
#  'Exit


while True:
    print("\nMenu:")
    print("1: Add")
    print("2: Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Action: Item added!")
    elif choice == '2':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
