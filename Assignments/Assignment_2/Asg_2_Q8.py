#  A program to find the factorial of a number using a loop
num = int(input("Enter a number:"))
i =1
fact = 1
# using loop
while i<=num:
    fact = fact * i
    i+=1
print("The factorial of number {} is {}" .format(num,fact) )
