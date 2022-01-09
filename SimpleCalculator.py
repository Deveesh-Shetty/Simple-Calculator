#Program to make a simple calculator
def addition(a,b):
    add = a + b
    print(add)

def subtraction(a,b):
    sub = a - b
    print(sub)

def multiplication(a,b):
    multiply = a*b
    print(multiply)

def division(a,b):
    if b != 0:
        divide = (a/b)
        print(divide)
    else:
        print("Can't divide by zero! Noob ")
    

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("""Enter a number between 1 to 4 where,
                  1 - Addition
                  2 - Subtraction
                  3 - Multiplication
                  4 - Division """)
choice = int(input("Enter your choice: "))
if choice == 1:
    addition(a,b)
elif choice == 2:
    subtraction(a,b)
elif choice == 3:
    multiplication(a,b)
elif choice == 4:
    division(a,b)
else:
    print("Choice not found! Enter a number between 1 - 4 ")
    
               
