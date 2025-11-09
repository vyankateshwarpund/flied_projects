#  A program to input a year and check whether it is a leap year or not. (if-else)
year = int(input("enter year :"))
#cheak condition

if year % 4 == 0:
    print("leap year")
else:
    print("not leap year")    