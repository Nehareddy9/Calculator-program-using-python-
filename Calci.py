print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
ch=int(input("Enter Choice(1-4): "))
if ch==1:
    a=float(input("Enter A:"))
    b=float(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=float(input("Enter A:"))
    b=float(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=float(input("Enter A:"))
    b=float(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=float(input("Enter A:"))
    b=float(input("Enter B:"))
    if(b!=0):
        c=a/b
    else:
        c="cannot divide by zero"
    print(c)
else:
    print("Invalid Choice"
