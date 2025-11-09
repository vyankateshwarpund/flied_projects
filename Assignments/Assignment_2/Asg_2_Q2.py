# 2.A program to input three numbers and find the greatest among them. (if-else)
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))

if num1>num2 and num1>num3:
    print("first number {} is greater number :" .format(num1))
elif num2>num3:
    print("second number {}is greater number :" .format(num2))    
else:
    print("Third {} is greater : " .format(num3))  