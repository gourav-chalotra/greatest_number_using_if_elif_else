num1=int(input('enter the first number: '))
num2=int(input("enter the the secound number: "))
num3=int(input("enter the third number: "))
num4=int(input("enter the fourth number: "))

if num1>num2:
    winner1=num1
elif num1<num2:
    winner1=num2
if num4<num3:
    winner2=num3
elif num4>num3:
    winner2=num4
if winner1>winner2:
    print(f"{winner1}is gratest number")
elif winner1<winner2:
    print(f"{winner2}is greatest number")
    