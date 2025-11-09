# A program to input the principal, rate, and time, and display the simple interest
prin = float(input("Enter principle amount in rs :"))
rate = float(input("Enter rate of instrest in % :"))
time = float(input("Enter time period in years :"))
#Formula of simple intrest
si = prin*rate*time
print(f"Simple intrest is : {si:.2f}")