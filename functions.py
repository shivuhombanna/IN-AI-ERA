# def calculater_area(lenth,width):
#     areas=lenth*width
#     return areas
# cal=calculater_area(4,8)
# # print(cal)

# Create four functions: add(a, b), subtract(a, b), multiply(a, b), divide(a, b)
# divide should handle division by zero — return a message instead of crashing
# Add docstrings to all four functions
# Use a while True loop with a menu:

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def divaid(a,b):
    return a/b

def display_menu():
    print("Welcom to calculater ")
    print(" 1.add \n 2.subtracion \n 3.multiplication \n 4.divide \n 5.quite")

while (True):
    display_menu()
    choice=int(input("  enter your choice "))

    a=int(input(" enter the first num "))
    b=int(input(" emter the secnd num "))

    if choice==1:
        print("result",add(a,b))
    elif choice==2:
        print("result",sub(a,b))
    elif choice==3:
        print("result",mult(a,b))
    elif choice==4:
        if a and b==0:
            print("ERORR")
        else:
            print("result",divaid(a,b))
    elif choice==5:
        print(" OK BYEEE !")
        break
    else:
        print("You have a weong choice can you repit again ")

