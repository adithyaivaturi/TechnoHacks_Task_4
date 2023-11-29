class calculator:
    def Add(a,b):
        return a+b
    def Subtract(a, b):
        return a-b
    def Multiply(a, b):
        return a*b
    def Divide(a, b):
        if b==0:
            print("Error! Cannot divide by zero")
        else:
            return a/b
while(True):
    print("Select The Option:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    opt=int(input("Enter The Option No : "))
    def inp():
        num1=int(input("Enter First Number : "))
        num2=int(input("Enter Second Number : "))
        return num1,num2
    if opt == 1 :
        num1,num2=inp()
        result = calculator.Add(num1,num2)
    elif opt == 2:
        num1,num2=inp()
        result = calculator.Subtract(num1,num2)
    elif opt == 3:
        num1,num2=inp()
        result = calculator.Multiply(num1,num2)
    elif opt == 4:
        num1,num2=inp()
        result = calculator.Divide(num1,num2)
    elif opt == 5:
        break
    else:
        result ="Invalid Option"
    print(result)
print("======Exit======")
